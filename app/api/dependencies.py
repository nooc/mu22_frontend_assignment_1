from app.service import Database
from app.service import Recipes
from fastapi import Depends


def db_dep() -> Database:
    return Database()

def recipes_dep(db:Database = Depends(db_dep)):
    return Recipes(db)
