from . import Database


class Recipes():
    
    def __init__(self, db:Database) -> None:
        self.db = db

    def get_recipes():
        pass
    
    def add_comment(recipe_id:int, text:str):
        pass


__all__ = ('Recipes', 'Recipe','Ingredient')
