from pydantic import BaseModel
from typing import Optional
from .ingredient import Ingredient
from .review import Review

class RecipeBase(BaseModel):
    title:str
    image:str
    summary:str
    details:str
    time:int
    num_default:int
    num_min:int
    num_max:int
    num_suffix:str

class Recipe(RecipeBase):
    id:Optional[int] = None
    ingredients:Optional[list[Ingredient]] = []
    instructions:Optional[list[str]] = []
    reviews:Optional[list[Review]] = []
