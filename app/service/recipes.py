import json

from app.model import (Ingredient, Instruction, IngredientBase,
                       InstructionBase, Recipe, RecipeBase, RecipeInput, ReviewBase,
                       Review, ReviewInput)
from fastapi import status, HTTPException
from . import Database


class Recipes():
    
    def __init__(self, db:Database):
        self.__db = db

    def get_recipes(self) -> list[Recipe]:
        results:list[Recipe] = []
        recipes = self.__db.get_all_objects('recipe')
        for row in recipes:
            rec = Recipe(
                id=row[0],
                title=row[1],
                url=row[2],
                image=row[3],
                summary=row[4],
                details=row[5],
                time=row[6],
                num_default=row[7],
                num_min=row[8],
                num_max=row[9],
                num_suffix=row[10]
            )
            for row in self.__db.query('ingredient','recipe_id = :id',{'id':rec.id}):
                rec.ingredients.append(IngredientBase(name=row[1], amount=row[2], unit=row[3]))
            for row in self.__db.query('instruction','recipe_id = :id',{'id':rec.id}):
                rec.instructions.append(InstructionBase(text=row[1]))
            for row in self.__db.query('review','recipe_id = :id',{'id':rec.id}):
                rec.reviews.append(ReviewBase(name=row[3], text=row[4],rating=row[5]))
            results.append(rec)
        return results
    
    def put_recipe(self, recipe:RecipeInput):
        """Import data to db.

        Args:
            recipe (RecipeInput): _description_
        """
        # put recipe
        recipe_dict = recipe.dict()
        new_recipe = RecipeBase(**recipe_dict)
        recipe_id = self.__db.put_object('recipe', new_recipe)
        # put ingredients
        for item in recipe.ingredients:
            new_ing = Ingredient(recipe_id = recipe_id, **item.dict())
            self.__db.put_object('ingredient', new_ing)
        # put instructions
        for item in recipe.instructions:
            new_inst = Instruction(recipe_id = recipe_id, **item.dict())
            self.__db.put_object('instruction', new_inst)
        # put reviews
        for item in recipe.reviews:
            new_rev_dict = item.dict()
            new_rev_dict['recipe_id'] = recipe_id
            new_rev = ReviewInput(**new_rev_dict)
            self.__db.put_object('review', new_rev)

    
    def add_review(self, review:ReviewInput) -> ReviewBase:
        id = self.__db.put_object('review', review)
        if not id:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return ReviewBase(**review.dict())


__all__ = ('Recipe','ReviewInput')
