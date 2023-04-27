from pydantic import BaseModel, AnyHttpUrl
from typing import Optional
from .ingredient import IngredientBase
from .review import ReviewInput, ReviewBase
from .instruction import InstructionBase

class RecipeBase(BaseModel):
    title:str
    url:AnyHttpUrl
    image:str
    summary:str
    details:str
    time:int
    num_default:int
    num_min:int
    num_max:int
    num_suffix:str

class RecipeInput(RecipeBase):
    ingredients:Optional[list[IngredientBase]] = []
    instructions:Optional[list[InstructionBase]] = []
    reviews:Optional[list[ReviewInput]] = []

class Recipe(RecipeBase):
    id:Optional[int] = None
    ingredients:Optional[list[IngredientBase]] = []
    instructions:Optional[list[InstructionBase]] = []
    reviews:Optional[list[ReviewBase]] = []
