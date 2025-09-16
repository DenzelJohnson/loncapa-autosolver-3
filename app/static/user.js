function mark(ok) { return ok ? "✓" : "✗"; }

function renderResults(report) {
  const container = document.getElementById("results");
  container.innerHTML = "";
  if (!report || !Array.isArray(report.questions)) {
    container.textContent = "No results";
    return;
  }
  report.questions.forEach((q) => {
    const card = document.createElement("div");
    card.className = "result-card";

    const title = document.createElement("div");
    title.className = "result-title";
    title.textContent = "Question:";
    card.appendChild(title);

    const qtext = document.createElement("div");
    qtext.className = "qtext";
    qtext.textContent = q.text || q.snippet || "";
    card.appendChild(qtext);

    const ansLabel = document.createElement("div");
    ansLabel.className = "result-title";
    ansLabel.textContent = "Answer:";
    card.appendChild(ansLabel);

    let anyOk = false;
    if (Array.isArray(q.solutions) && q.solutions.length) {
      // For multipart, display each part on separate line
      q.solutions.sort((a,b)=>(a.part||0)-(b.part||0)).forEach((sol)=>{
        const row = document.createElement("div");
        row.style.display = "flex";
        row.style.alignItems = "center";
        row.style.justifyContent = "space-between";
        const leftWrap = document.createElement("div");
        const partLabel = document.createElement("div");
        partLabel.className = "result-title";
        partLabel.textContent = sol.prompt ? sol.prompt : (sol.part ? `Part ${sol.part}` : "");
        const left = document.createElement("div");
        left.className = "answer";
        left.textContent = sol.ok ? (sol.display || String(sol.value)) : (sol.error || "failed");
        leftWrap.appendChild(partLabel);
        leftWrap.appendChild(left);
        const btn = document.createElement("button");
        btn.className = "btn btn-outline copy";
        btn.innerHTML = "<span>📋</span> Copy";
        btn.onclick = () => navigator.clipboard.writeText(sol.ok ? (sol.display || String(sol.value)) : (sol.error || ""));
        row.appendChild(leftWrap);
        row.appendChild(btn);
        card.appendChild(row);
        if (sol.ok) anyOk = true;
      });
    } else {
      // Single-part fallback
      const single = document.createElement("div");
      single.className = "answer";
      if (q.steps && q.steps.solution && q.steps.solution.ok) {
        single.textContent = q.steps.solution.display || String(q.steps.solution.value);
        anyOk = true;
      } else {
        single.textContent = (q.steps && q.steps.solution && q.steps.solution.error) || "failed";
      }
      const btn = document.createElement("button");
      btn.className = "btn btn-outline copy";
      btn.innerHTML = "<span>📋</span> Copy";
      btn.onclick = () => navigator.clipboard.writeText(single.textContent);
      const row = document.createElement("div");
      row.style.display = "flex";
      row.style.alignItems = "center";
      row.style.justifyContent = "space-between";
      row.appendChild(single);
      row.appendChild(btn);
      card.appendChild(row);
    }

    container.appendChild(card);
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

window.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("solve-assignment");
  if (btn) btn.addEventListener("click", solve);
}); 