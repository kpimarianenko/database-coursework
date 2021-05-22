from repositories.base_repository import BaseRepository
from database.connection import db

subjects_repo = BaseRepository(db['subjects'])
