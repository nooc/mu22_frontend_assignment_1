import json

from app.model import Recipe, Review, ReviewInput

from . import Database


class Recipes():
    
    def __init__(self, db:Database):
        self.__db = db

    def get_recipes(self) -> list[Recipe]:
        #TODO: Use database
        result = []
        with open('recipes.json','rb') as f:
            recipes = json.load(f)
            for recipe in recipes:
                result.append(Recipe(**recipe))
        return result
    
    def add_review(self, recipy_id:int, review:ReviewInput) -> Review:
        self.__db.put_object('review', review.dict())
        return Review(**review)


__all__ = ('Recipe','ReviewInput')
