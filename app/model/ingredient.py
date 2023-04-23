from pydantic import BaseModel

class Ingredient(BaseModel):
    name:str
    amount:float
    unit:str
