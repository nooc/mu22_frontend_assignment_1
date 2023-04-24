import json

from app.model import Recipe
from app.model import Ingredient
from app.model import Review

from . import Database


class Recipes():
    
    def __init__(self, db:Database):
        self.__db = db

    def get_recipes(self) -> list[Recipe]:
        with open('recipes.json','rb') as f:
            data = json.load(f)
        result = []
        for recipe in data:
            r = Recipe(**recipe)
            for ing in recipe['ingredients']:
                r.ingredients.append(Ingredient(**ing))
            r.instructions = recipe['instructions']
            for rev in recipe['reviews']:
                r.reviews.append(Review(**rev))
            result.append(r)
        return result
    
    def add_review(self, recipe_id:int, text:str):
        pass


__all__ = ('Recipes', 'Recipe','Ingredient')
