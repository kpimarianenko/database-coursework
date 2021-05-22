from repositories.base_repository import BaseRepository
from database.connection import db

marks_repo = BaseRepository(db['marks'])
