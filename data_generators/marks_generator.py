import uuid
from faker import Faker
from data_generators.utils import write_generated_data
from repositories.marks_repository import marks_repo

faker = Faker()
Faker.seed('marks')


def generate_marks(student_id, subject_id, quantity=10):
    marks = []

    for i in range(quantity):
        marks.append({
            '_id': f'{uuid.uuid4()}',
            'value': faker.random_int(0, 100),
            'student_id': student_id,
            'subject_id': subject_id
        })
    write_generated_data(marks_repo, marks)
    return marks
