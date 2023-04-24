from typing import Optional
from pydantic import BaseModel

class Review(BaseModel):
    author:str
    text:str
    rating:int

class ReviewDb(Review):
    id:Optional[int] = None
    user_id:int
    recipe_id:int
