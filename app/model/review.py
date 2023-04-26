from typing import Optional
from pydantic import BaseModel

class Review(BaseModel):
    name:str
    text:str
    rating:int

class ReviewInput(Review):
    email:int

class ReviewDb(ReviewInput):
    id:Optional[int] = None
    recipe_id:int
