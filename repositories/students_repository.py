from repositories.base_repository import BaseRepository
from database.connection import db


class StudentsRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def get_ages(self):
        return self.collection.distinct('age')


students_repo = StudentsRepository(db['students'])
