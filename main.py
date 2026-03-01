from fastapi import FastAPI
from database import engine, Base
from routes import produtos
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

app.include_router(produtos.router)

@app.get("/interface", response_class=HTMLResponse)
def interface(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
def home():
    return {"mensagem": "API organizada em camadas 🚀"}

@app.get("/debug")
def debug():
    return {"funcionando": True}