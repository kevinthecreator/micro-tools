from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random, re
import lorem

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/tools/password", response_class=HTMLResponse)
async def password_generator(request: Request):
    return templates.TemplateResponse("tools/password.html", {"request": request, "password": None})

@app.post("/tools/password", response_class=HTMLResponse)
async def generate_password(request: Request, length: int = Form(...)):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choices(chars, k=length))
    return templates.TemplateResponse("tools/password.html", {"request": request, "password": password})

@app.get("/tools/slug", response_class=HTMLResponse)
async def slug_formatter(request: Request):
    return templates.TemplateResponse("tools/slug.html", {"request": request, "slug": None})

@app.post("/tools/slug", response_class=HTMLResponse)
async def generate_slug(request: Request, text: str = Form(...)):
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower().strip().replace(" ", "-")
    return templates.TemplateResponse("tools/slug.html", {"request": request, "slug": slug})

@app.get("/tools/lorem", response_class=HTMLResponse)
async def lorem_view(request: Request):
    return templates.TemplateResponse("tools/lorem.html", {"request": request, "paragraphs": None})

@app.post("/tools/lorem", response_class=HTMLResponse)
async def lorem_gen(request: Request, count: int = Form(...)):
    paras = [lorem.paragraph() for _ in range(count)]
    return templates.TemplateResponse("tools/lorem.html", {"request": request, "paragraphs": paras})

@app.get("/tools/email-extractor", response_class=HTMLResponse)
async def email_extractor(request: Request):
    return templates.TemplateResponse("tools/email_extractor.html", {"request": request, "emails": None})

@app.post("/tools/email-extractor", response_class=HTMLResponse)
async def extract_emails(request: Request, input_text: str = Form(...)):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', input_text)
    return templates.TemplateResponse("tools/email_extractor.html", {"request": request, "emails": emails})

@app.get("/tools/unit-converter", response_class=HTMLResponse)
async def unit_converter(request: Request):
    return templates.TemplateResponse("tools/unit_converter.html", {"request": request, "result": None})

@app.post("/tools/unit-converter", response_class=HTMLResponse)
async def convert_units(request: Request, value: float = Form(...), unit: str = Form(...)):
    result = None
    if unit == "km-miles":
        result = round(value * 0.621371, 4)
    elif unit == "miles-km":
        result = round(value / 0.621371, 4)
    elif unit == "kg-lbs":
        result = round(value * 2.20462, 4)
    elif unit == "lbs-kg":
        result = round(value / 2.20462, 4)
    return templates.TemplateResponse("tools/unit_converter.html", {"request": request, "result": result})
