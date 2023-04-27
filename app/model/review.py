from typing import Optional
from pydantic import BaseModel, EmailStr

class ReviewBase(BaseModel):
    name:str
    text:str
    rating:int

class Review(ReviewBase):
    recipe_id:int

class ReviewInput(ReviewBase):
    email:EmailStr
    recipe_id:Optional[int] = None

class ReviewDb(ReviewInput):
    id:Optional[int] = None
