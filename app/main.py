"""
Primary FastPI application
"""
from fastapi import FastAPI
from app.api.endpoints import api_routes
from .config import settings
from fastapi.staticfiles import StaticFiles

def create_app():
    '''Initialize FastAPI app'''
    app = FastAPI(
        title = settings.TITLE,
        description = settings.DESCRIPTION,
        openapi_url = settings.OPENAPI_URL,
        docs_url = settings.DOCS_URL,
        redoc_url = None)

    app.include_router(api_routes)
    
    app.mount("/", StaticFiles(directory="www"), name="www")

    return app


application = create_app()
