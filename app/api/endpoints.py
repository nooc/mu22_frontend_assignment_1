import sqlite3
from typing import Any

from fastapi import APIRouter, Body, Depends, status, HTTPException
from starlette.responses import RedirectResponse

from app.model import Recipe, ReviewBase, ReviewInput, RecipeInput
from app.service import Recipes

from .dependencies import recipes_dep

# Init FastAPI router for API endpoints
api_routes = APIRouter()


@api_routes.get('/', include_in_schema=False)
def redirect_to_docs():
    """Redirect to API docs when at site root"""
    return RedirectResponse('/index.html')


@api_routes.get(
    '/recipes',
    description='Get list of recipes.',
    response_model=list[Recipe]
)
def get_recipes(
    repo:Recipes = Depends(recipes_dep)
) -> Any:
    return repo.get_recipes()

@api_routes.post(
    '/recipes',
    description='Post list of recipes.'
)
def post_recipes(
    recipes:list[RecipeInput] = Body(),
    repo:Recipes = Depends(recipes_dep)
) -> Any:
    for recipe in recipes:
        repo.put_recipe(recipe)
    return 'OK'

@api_routes.post(
    '/review',
    description='Post a review for recipe.',
    response_model=ReviewBase
)
def post_review(
    review:ReviewInput = Body(),
    repo:Recipes = Depends(recipes_dep)
) -> Any:
    try:
        return repo.add_review(review)
    except sqlite3.IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
