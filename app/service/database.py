import sqlite3
from typing import Any
from app.config import settings

class Database():

    __schema=[
        '''CREATE TABLE IF NOT EXISTS "recipe" (
    "id"	INTEGER NOT NULL,
    "title"	TEXT NOT NULL,
    "summary"	TEXT NOT NULL,
    "details"	TEXT,
    "time"	INTEGER NOT NULL,
    "num_default"	INTEGER NOT NULL,
    "num_min"	INTEGER NOT NULL,
    "num_max"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)''',
        '''CREATE TABLE IF NOT EXISTS "review" (
    "id"	INTEGER NOT NULL,
    "user_id"	INTEGER NOT NULL,
    "recipe_id"	INTEGER NOT NULL,
    "author"	TEXT NOT NULL,
    "text"	TEXT NOT NULL,
    "rating"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)''',
        '''CREATE TABLE IF NOT EXISTS "user" (
    "id"	INTEGER NOT NULL,
    "name"	TEXT NOT NULL,
    "email"	TEXT NOT NULL UNIQUE,
    "password"	TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)''',
        '''CREATE TABLE IF NOT EXISTS "ingredient" (
    "id"	INTEGER NOT NULL,
    "name"	TEXT NOT NULL,
    "amount"	INTEGER NOT NULL,
    "unit"	TEXT,
    "recipe_id"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("recipe_id") REFERENCES "recipe"("id") on delete cascade
)'''
    ]

    __db:sqlite3.Connection = None

    def __init__(self):
        self.__con = sqlite3.connect(settings.DB_FILE)
        self.__cur = self.__con.cursor()
        # create schema
        
        for create_statement in self.__schema:
            self.__cur.execute(create_statement)
        self.__con.commit()
            

    def get_object(self, type:str, id:Any) -> Any:
        with self.__con.execute(f'select * from ? where id = ?', parameters=(type, id)) as c:
            return c.fetchone()

    def get_all_objects(self, type:str) -> Any:
        with self.__con.execute(f'select * from ?', parameters=(type)) as c:
            return c.fetchall()

    def put_object(self, type:str, item):
        self.__con.execute(f'insert into ? values ?', [item])
        self.__con.commit()
