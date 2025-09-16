from typing import List, Dict, Optional
import re
from bs4 import BeautifulSoup, NavigableString, Tag

# Anchor names are percent-encoded and contain "problem" as plain text (e.g., sf%2dprob1508%2eproblem)
PROBLEM_ANCHOR_RE = re.compile(r"problem", re.IGNORECASE)
SYM_INPUT_NAME_RE = re.compile(r"_symb$")
# Try to capture the trailing *.problem segment anywhere in the value
PROBLEM_ID_RE = re.compile(r"([^/]+\.problem)(?:$|[?#])", re.IGNORECASE)


def _extract_problem_id(font_node: Tag) -> Optional[str]:
    # Hidden input with *_symb contains a value including the resource path ending in *.problem
    for inp in font_node.find_all("input"):
        name = inp.get("name", "")
        if SYM_INPUT_NAME_RE.search(name):
            value = inp.get("value", "")
            m = PROBLEM_ID_RE.search(value)
            if m:
                return m.group(1)
    return None


def _extract_statement_text(font_node: Tag) -> str:
    # Gather text until we reach the first part anchor <a name="1"> or first answer table
    parts: List[str] = []
    for node in font_node.descendants:
        if isinstance(node, Tag):
            if node.name == "a" and node.get("name") == "1":
                break
            if node.name == "table":
                break
            # Skip any text inside script/style tags entirely
            if node.name in ("script", "style"):
                continue
        elif isinstance(node, NavigableString):
            # Ignore strings that belong to script/style parents
            parent = node.parent
            if isinstance(parent, Tag) and parent.name in ("script", "style"):
                continue
            parts.append(str(node))
    text = " ".join(p.strip() for p in parts if p.strip())
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Strip the leading LON-CAPA timing JS blob if present
    text = re.sub(
        r"^var\s+serverDueDate=.*?;\s*var\s+serverTime=.*?;\s*var\s+clientTime=.*?;\s*var\s+dueDate=.*?;\s*",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return text


def _extract_part_texts(font_node: Tag) -> List[str]:
    """Collect texts for each part starting at anchors name="1","2",... using the
    prompt text that appears immediately BEFORE each anchor in LON-CAPA HTML.
    Returns a list of cleaned strings in numeric order for parts >= 2.
    """
    part_texts: List[str] = []
    anchors = [a for a in font_node.find_all("a") if a.get("name", "").isdigit()]
    anchors.sort(key=lambda a: int(a.get("name")))
    # Skip the first anchor (its prompt is already included in the preface statement)
    for a in anchors[1:]:
        collected_rev: List[str] = []
        cursor = a.previous_sibling
        while cursor is not None:
            if isinstance(cursor, Tag):
                if cursor.name in ("script", "style"):
                    cursor = cursor.previous_sibling
                    continue
                # Stop at previous answer/table or previous anchor boundary
                if cursor.name == "table":
                    break
                if cursor.name == "a" and cursor.get("name", "").isdigit():
                    break
                collected_rev.append(cursor.get_text(" ", strip=True))
            elif isinstance(cursor, NavigableString):
                collected_rev.append(str(cursor).strip())
            cursor = cursor.previous_sibling
        # reverse to restore original order
        text = " ".join(t for t in reversed([t for t in collected_rev if t]))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            part_texts.append(text)
    return part_texts


def extract_questions(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    results: List[Dict[str, str]] = []

    for anchor in soup.find_all("a"):
        name_attr = anchor.get("name", "")
        if not name_attr:
            continue
        if not PROBLEM_ANCHOR_RE.search(name_attr):
            continue
        # The question content typically resides in the following <font> node; provide a fallback
        font_node = anchor.find_next("font")
        if not font_node:
            # Fallback: use the next sibling container
            font_node = anchor.find_next()
            if not isinstance(font_node, Tag):
                continue
        problem_id = _extract_problem_id(font_node) or ""
        # Extra fallback: try to read any *.problem substring around the anchor if not found
        if not problem_id:
            around_text = (anchor.get("name", "") + " " + font_node.get_text(" ", strip=True))
            m2 = PROBLEM_ID_RE.search(around_text)
            if m2:
                problem_id = m2.group(1)
        statement = _extract_statement_text(font_node)
        # Append any part texts after the preface to show all sub-questions
        part_texts = _extract_part_texts(font_node)
        if part_texts:
            statement = (statement + " " + " ".join(part_texts)).strip()
        snippet = statement[:200] + ("…" if len(statement) > 200 else "")
        results.append({
            "problem_id": problem_id,
            "text": statement,
            "snippet": snippet,
        })

    return results 