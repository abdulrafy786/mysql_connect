from fastapi import FastAPI,HTTPException , Request
from fastapi.responses import HTMLResponse
from database_connect import engine , Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.post("/")
def read_root():
    return {"Abdul ": "Khan"}

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse )
async def read_item(request: Request):
   return templates.TemplateResponse("index.html" , {"request": request})

@app.post("/items")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255))
    price = Column(Float)

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


