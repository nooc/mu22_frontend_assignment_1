from typing import Optional
from pydantic import BaseModel


class Ingredient(BaseModel):
    name:str
    amount:float
    unit:Optional[str] = None

class IngredientDb(Ingredient):
    id:Optional[int] = None
