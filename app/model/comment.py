from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    user_id:int
    recipe_id:int

    text:str
