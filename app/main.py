from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.pipeline import solve_assignment
from app.html_parser import extract_questions

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/user", response_class=HTMLResponse)
def user_page(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})

@app.post("/debug-extract")
async def debug_extract_endpoint(payload: dict):
    html = payload.get("html", "")
    items = extract_questions(html)
    return JSONResponse(items)

@app.post("/solve-assignment")
async def solve_assignment_endpoint(payload: dict):
    html = payload.get("html", "")
    report = solve_assignment(html)
    return JSONResponse(report)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
