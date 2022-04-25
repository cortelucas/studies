from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Client(BaseModel):
    name: str


class Product(BaseModel):
    name: str
    price: float


@app.get("/")
async def root():
    return {"message": "Olá FastAPI"}


@app.get("/ola/{nome}")
def hello(name: str) -> str:
    msg: str = f"Olá {name}, tudo numa boa?"
    return {"message": msg}


@app.get("/profile")
async def profile():
    return {"name": "Profile"}


@app.post("/profile")
async def sign_up():
    return {"message": "Created Profile"}


@app.put("/profile")
async def update_profile():
    return {"message": "Updated Profile"}


@app.delete("/profile")
async def delete_profile():
    return {"message": "Deleted Profile"}


# Parametro de rotas
@app.get("/quadrado/{number}")
def number_squad(number: int) -> int:
    squad: int = number * number
    msg: str = f"O quadrado de {number} é {squad}"

    return {"message": msg}


# Parametro de rotas com query strings
@app.get("/dobro")
def double_value(value: int) -> int:
    result: int = value * 2
    return {"result": f"O dobro de {value} é {result}"}


@app.get("/area-retangulo")
def area_ret(alt: int, larg: int) -> int:
    area = larg * alt
    return {"area": area}


@app.post("/produtos")
def products(product: Product) -> Product:
    return {"product": product}
