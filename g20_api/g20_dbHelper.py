#!/usr/bin/env python
from pymongo import MongoClient


def db_init():
    db_name = ''
    conn = MongoClient('')
    db = conn.get_database(db_name)
    return db


def db_init_dm5():
    db_name = ''
    conn = MongoClient('')
    db = conn.get_database(db_name)
    return db
