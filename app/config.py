from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE = 'Recept Hjälparen'
    DESCRIPTION = 'Se, justera och kommentera recept.'
    OPENAPI_URL = '/api-spec/openapi.json'
    DOCS_URL = '/api-doc'

    DB_FILE: Optional[str] = 'data.sqlite'

settings = Settings()
