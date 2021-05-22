import uuid
from faker import Faker
from data_generators.utils import write_generated_data
from repositories.subjects_repository import subjects_repo

faker = Faker()
Faker.seed('subjects')


def generate_subjects(quantity=10):
    subjects = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)

        subjects.append({
            '_id': f'{uuid.uuid4()}',
            'name': name,
        })
    write_generated_data(subjects_repo, subjects)
    return subjects
