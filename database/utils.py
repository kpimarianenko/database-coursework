from database.connection import db


def drop():
    db['groups'].drop()
    db['subjects'].drop()
    db['students'].drop()
    db['marks'].drop()
