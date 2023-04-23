import sqlite3
from typing import Any
from app.config import settings

class Database():

    __db:sqlite3.Connection = None

    def __init__(self):
        self.__db = sqlite3.connect(settings.DB_FILE)

    def get_object(self, type:str, id:Any) -> Any:
        with self.__db.execute(f'select * from ? where id = ?', parameters=(type, id)) as c:
            return c.fetchone()

    def get_all_objects(self, type:str) -> Any:
        with self.__db.execute(f'select * from ?', parameters=(type)) as c:
            return c.fetchall()

