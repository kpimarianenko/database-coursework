import uuid
from faker import Faker
from data_generators.utils import write_generated_data
from repositories.students_repository import students_repo

faker = Faker()


def generate_students(group_id, quantity=10):
    students = []

    for i in range(quantity):
        students.append({
            '_id': f'{uuid.uuid4()}',
            'name': faker.name(),
            'age': faker.random_int(16, 25),
            'group_id': group_id
        })
    write_generated_data(students_repo, students)
    return students
