from repositories.base_repository import BaseRepository
from database.connection import db

groups_repo = BaseRepository(db['groups'])
