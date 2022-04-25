from typing import List, Optional
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Animal(BaseModel):
    id: Optional[str]
    name: str
    age: int
    sex: str
    color: str


db: List[Animal] = []


@app.get("/animais")
async def get_animals():
    return {"animals": db}


@app.get("/animais/{animal_id: str}")
async def get_animal_by_id(animal_id: str) -> Animal:
    for animal in db:
        if animal.id == animal_id:
            return {"animal": animal}
    return {"error": "Animal not found"}


@app.post("/animais")
async def create_animal(animal: Animal) -> Animal:
    animal.id = str(uuid4().hex)
    db.append(animal)
    return {"message": "Animal created successfully", "animal": animal}


# @app.put("/animais/{animal_id: str}")
# async def update_animal(animal_id: str, animal: Animal) -> Animal:
#     return


@app.delete("/animais/{animal_id: str}")
async def delete_animal(animal_id: str) -> str:
    position: int = -1
    for index, animal in enumerate(db):
        if animal.id == animal_id:
            position = index
            break

    if position != -1:
        db.pop(position)
        return {"message": "Animal deleted"}
    else:
        return {"error": "Animal not found"}
