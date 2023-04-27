from typing import Optional

from pydantic import BaseModel


class IngredientBase(BaseModel):
    name:str
    amount:float
    unit:Optional[str] = None

class Ingredient(IngredientBase):
    recipe_id:Optional[int] = None

class IngredientDb(Ingredient):
    id:Optional[int] = None
