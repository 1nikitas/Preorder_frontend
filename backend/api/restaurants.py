from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Restaurant(BaseModel):
    name: str
    rating: float
    ratings: int
    distance: float
    img: str

@app.get("/restaurants", response_model=List[Restaurant])
async def read_restaurants():
    return [
        {"name": "Restaurant 1", "rating": 4.5, "ratings": 200, "distance": 2.5, "img": "link_to_image_1"},
        {"name": "Restaurant 2", "rating": 4.8, "ratings": 350, "distance": 1.9, "img": "link_to_image_2"}
    ]
