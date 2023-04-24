from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from starlette.responses import RedirectResponse

from app.model import Recipe
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
