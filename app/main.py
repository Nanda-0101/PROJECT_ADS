from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# static file (CSS + JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# template HTML
templates = Jinja2Templates(directory="templates")


# ROUTE LOGIN
@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})