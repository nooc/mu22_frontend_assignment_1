import sqlite3
from typing import Any

from pydantic import BaseModel
from app.config import settings

class Database():

    __schema=[
        '''CREATE TABLE IF NOT EXISTS "recipe" (
    "id"	INTEGER NOT NULL,
    "title"	TEXT NOT NULL,
    "image"	TEXT NOT NULL,
    "summary"	TEXT NOT NULL,
    "details"	TEXT,
    "time"	INTEGER NOT NULL,
    "num_default"	INTEGER NOT NULL,
    "num_min"	INTEGER NOT NULL,
    "num_max"	INTEGER NOT NULL,
    "num_suffix"	TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)''',
        '''CREATE TABLE IF NOT EXISTS "review" (
    "id"	INTEGER NOT NULL,
    "recipe_id"	INTEGER NOT NULL,
    "email"	TEXT NOT NULL UNIQUE,
    "name"	TEXT NOT NULL,
    "text"	TEXT NOT NULL,
    "rating"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("recipe_id") REFERENCES "recipe"("id") on delete cascade
)''',
        '''CREATE TABLE IF NOT EXISTS "ingredient" (
    "id"	INTEGER NOT NULL,
    "name"	TEXT NOT NULL,
    "amount"	INTEGER NOT NULL,
    "unit"	TEXT,
    "recipe_id"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("recipe_id") REFERENCES "recipe"("id") on delete cascade
)''',
        '''CREATE TABLE IF NOT EXISTS "instruction" (
    "id"	INTEGER NOT NULL,
    "text"	TEXT NOT NULL,
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
        cur = self.__con.execute(f'select * from ? where id = ?', (type, id))
        return cur.fetchone()

    def get_all_objects(self, type:str) -> Any:
        cur = self.__con.execute(f'select * from {type}')
        return cur.fetchall()
    
    def query(self, type:str, where:str, params:dict) -> Any:
        cur = self.__con.execute(f'select * from {type} where {where}', params)
        return cur.fetchall()

    def put_object(self, type:str, item:BaseModel) -> int:
        itm_d = item.dict()
        cols = ','.join(itm_d.keys())
        vals = ','.join(['?']*len(itm_d))
        cur = self.__con.execute(f'insert into {type} ({cols}) values ({vals})', list(itm_d.values()))
        row_id = cur.lastrowid
        self.__con.commit()
        return row_id
