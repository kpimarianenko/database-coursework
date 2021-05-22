import numpy as np
from repositories.base_repository import BaseRepository
from database.connection import db
from repositories.students_repository import students_repo


class MarksRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def get_marks_by_group(self, group_id):
        marks = []
        students = students_repo.find({'group_id': group_id})

        for s in students:
            student_marks = self.find({'student_id': s['_id']})
            marks = np.append(marks, student_marks)
        return marks

    def get_marks_by_group_and_subject(self, group_id, subject_id):
        marks = []
        students = students_repo.find({'group_id': group_id})

        for s in students:
            student_marks = self.find({'student_id': s['_id'], 'subject_id': subject_id})
            marks = np.append(marks, student_marks)
        return marks


marks_repo = MarksRepository(db['marks'])
