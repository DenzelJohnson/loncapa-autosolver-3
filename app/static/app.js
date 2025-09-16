function mark(ok) {
  return ok ? "✓" : "✗";
}

function renderResults(report) {
  try { console.log('renderResults v=4 start'); } catch(_) {}

  const container = document.getElementById("results");
  container.innerHTML = "";
  if (!report || !Array.isArray(report.questions)) {
    container.textContent = "No results";
    return;
  }
  report.questions.forEach((q) => {
    const div = document.createElement("div");
    div.className = "box";

    const title = document.createElement("div");
    title.innerHTML = `<strong>${q.problem_id || "(unknown id)"}</strong><br><small>${q.text || q.snippet || ""}</small>`;
    div.appendChild(title);

    const steps = q.steps || {};

    const s1 = document.createElement("div");
    s1.textContent = `${mark(steps.extract && steps.extract.ok)} Questions Extracted${q.problem_id ? ` (${q.problem_id})` : ""}`;
    div.appendChild(s1);

    const s2 = document.createElement("div");
    if (steps.variables && steps.variables.ok) {
      s2.textContent = `${mark(true)} Variables Extracted: [${(steps.variables.vars || []).join(", ")}]`;
    } else {
      s2.textContent = `${mark(false)} Variables Extracted: ${(steps.variables && steps.variables.error) || "failed"}`;
    }
    div.appendChild(s2);

    // Render solutions (multipart aware)
    let allOk = true;
    if (Array.isArray(q.solutions) && q.solutions.length > 0) {
      q.solutions
        .sort((a, b) => (a.part || 0) - (b.part || 0))
        .forEach((sol) => {
          if (!sol.ok) allOk = false;
          const row = document.createElement("div");
          const label = sol.prompt ? `${sol.prompt}` : `Part ${sol.part || ""}`;
          if (sol.ok) {
            row.textContent = `${mark(true)} ${label}: ${sol.display || sol.value}`;
          } else {
            row.textContent = `${mark(false)} ${label}: ${sol.error || "failed"}`;
          }
          div.appendChild(row);
        });
    } else {
      const s3 = document.createElement("div");
      if (steps.solution && steps.solution.ok) {
        s3.textContent = `${mark(true)} Solution: ${steps.solution.display || steps.solution.value}`;
      } else {
        s3.textContent = `${mark(false)} Solution: ${(steps.solution && steps.solution.error) || "failed"}`;
        allOk = false;
      }
      div.appendChild(s3);
    }

    // Color the box based on overall success
    div.classList.add(allOk ? "success" : "failure");
    // Also set an explicit border so it stands out regardless of cached CSS
    const borderColor = allOk ? "#16a34a" : "#dc2626";
    div.style.border = `3px solid ${borderColor}`;
    try { console.log('box status', { allOk, borderColor, className: div.className }); } catch(_) {}

    container.appendChild(div);
  });
}

async function solve() {
  const btn = document.getElementById("solve-assignment");
  const loading = document.getElementById("loading");
  const html = document.getElementById("assignment-html").value;
  if (loading) loading.style.display = "block";
  if (btn) btn.disabled = true;
  try {
    const res = await fetch("/solve-assignment", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ html })
    });
    const data = await res.json();
    renderResults(data);
  } catch (e) {
    renderResults({ questions: [] });
  } finally {
    if (loading) loading.style.display = "none";
    if (btn) btn.disabled = false;
  }
}

async function debugExtract() {
  const html = document.getElementById("assignment-html").value;
  const res = await fetch("/debug-extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ html })
  });
  const data = await res.json();
  const container = document.getElementById("results");
  container.textContent = JSON.stringify(data, null, 2);
}

window.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("solve-assignment");
  if (btn) btn.addEventListener("click", solve);
  const dbg = document.getElementById("debug-extract");
  if (dbg) dbg.addEventListener("click", debugExtract);
});
