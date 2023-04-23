from pydantic import BaseModel
from .ingredient import Ingredient

class Recipe(BaseModel):
    id:int
    title:str
    desc_short:str
    desc_detail:str
    ingredients:list[Ingredient]
