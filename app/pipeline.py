from typing import Any, Dict, List
from app.html_parser import extract_questions
from app.pattern_matchers import REGISTRY as MATCHERS
from app.solution_functions import CATALOG_GROUPED_BY_ID
import importlib
from math import log10, floor, isfinite


def format_sig_figs(value: float, sig: int = 3) -> str:
    if not isfinite(value):
        return str(value)
    if value == 0:
        # 0 with sig figs -> 0.00 for sig=3
        return f"{0:.{sig-1}f}"
    abs_v = abs(value)
    decimals = sig - 1 - floor(log10(abs_v))
    # Round and format with fixed decimals so trailing zeros are kept
    if decimals > 0:
        return f"{round(value, decimals):.{decimals}f}"
    else:
        # No fractional digits; round to the appropriate 10^k
        return f"{int(round(value, decimals))}"


def solve_assignment(html: str) -> Dict[str, Any]:
    extracted = extract_questions(html)
    report: dict[str, Any] = {"questions": []}

    solvers_module = importlib.import_module("app.solution_functions")

    for q in extracted:
        problem_id = q.get("problem_id", "")
        text = q.get("text", "")
        snippet = q.get("snippet", "")
        item: dict[str, Any] = {"problem_id": problem_id, "text": text, "snippet": snippet, "steps": {}, "solutions": []}

        item["steps"]["extract"] = {"ok": True}

        entries = CATALOG_GROUPED_BY_ID.get(problem_id, [])
        if not entries:
            item["steps"]["variables"] = {"ok": False, "error": "no catalog entry"}
            report["questions"].append(item)
            continue

        entry0 = entries[0]
        matcher_name = entry0.get("pattern_matcher")
        matcher_fn = MATCHERS.get(matcher_name) if matcher_name else None
        if not matcher_fn:
            item["steps"]["variables"] = {"ok": False, "error": "no matcher"}
            report["questions"].append(item)
            continue

        try:
            variables_list = matcher_fn(q.get("text", ""))
            item["steps"]["variables"] = {"ok": True, "vars": variables_list}
        except Exception as e:
            item["steps"]["variables"] = {"ok": False, "error": str(e)}
            report["questions"].append(item)
            continue

        for entry in sorted(entries, key=lambda e: e.get("part") or 0):
            solver_name = entry.get("function")
            inputs_order = entry.get("inputs", [])
            units = entry.get("answer_units", "")
            solver_fn = getattr(solvers_module, solver_name, None)
            if not callable(solver_fn):
                item["solutions"].append({"ok": False, "error": "no solver", "part": entry.get("part"), "prompt": entry.get("prompt")})
                continue
            # Support matchers that return list-of-lists for multipart intervals
            part_vars = variables_list
            if isinstance(variables_list, list) and variables_list and isinstance(variables_list[0], list):
                # Select per-part variables if available; otherwise fall back to first pair
                idx = (entry.get("part") or 1) - 1
                if 0 <= idx < len(variables_list):
                    part_vars = variables_list[idx]
                else:
                    part_vars = variables_list[0]
            kwargs = {inputs_order[i]: part_vars[i] for i in range(min(len(inputs_order), len(part_vars)))}
            try:
                value = solver_fn(**{k: float(v) for k, v in kwargs.items()})
                display = f"{format_sig_figs(value, 3)} {units}".strip()
                item["solutions"].append({"ok": True, "value": value, "display": display, "part": entry.get("part"), "prompt": entry.get("prompt")})
            except Exception as e:
                item["solutions"].append({"ok": False, "error": str(e), "part": entry.get("part"), "prompt": entry.get("prompt")})

        report["questions"].append(item)

    return report
