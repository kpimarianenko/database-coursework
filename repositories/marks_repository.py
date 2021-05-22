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

    def get_marks_by_student_age(self, age):
        marks = []
        students = students_repo.find({'age': age})

        for s in students:
            student_marks = self.find({'student_id': s['_id']})
            marks = np.append(marks, student_marks)
        return marks

    def get_group_marks_count(self, group_id):
        count = 0
        students = students_repo.find({'group_id': group_id})

        for s in students:
            student_marks_count = len(self.find({'student_id': s['_id']}))
            count += student_marks_count
        return count


marks_repo = MarksRepository(db['marks'])
