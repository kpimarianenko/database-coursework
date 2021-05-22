from repositories.base_repository import BaseRepository
from database.connection import db

students_repo = BaseRepository(db['students'])