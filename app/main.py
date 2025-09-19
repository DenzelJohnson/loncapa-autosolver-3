from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.pipeline import solve_assignment
from app.html_parser import extract_questions
import os, json, datetime
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr

# Load .env if present (no-op in prod if env vars are already set)
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

class EmailIn(BaseModel):
    email: EmailStr

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

# Email capture → Google Sheets

def _gspread_client_from_env():
    try:
        import gspread
    except ImportError:
        raise HTTPException(status_code=500, detail="gspread not installed")
    svc_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not svc_json:
        raise HTTPException(status_code=500, detail="Missing GOOGLE_SERVICE_ACCOUNT_JSON")
    try:
        creds_dict = json.loads(svc_json)
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid GOOGLE_SERVICE_ACCOUNT_JSON")
    try:
        return gspread.service_account_from_dict(creds_dict)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to init Google client")

@app.post("/save-email")
async def save_email(payload: EmailIn, request: Request):
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    worksheet_name = os.environ.get("GOOGLE_SHEET_WORKSHEET", "Sheet1")
    if not sheet_id:
        raise HTTPException(status_code=500, detail="Missing GOOGLE_SHEET_ID")

    gc = _gspread_client_from_env()
    sh = gc.open_by_key(sheet_id)
    try:
        ws = sh.worksheet(worksheet_name)
    except Exception:
        ws = sh.sheet1

    ip = request.client.host if request and request.client else ""
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    try:
        ws.append_row([ts, payload.email, ip], value_input_option="USER_ENTERED")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to append row")
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
