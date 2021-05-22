import uuid
from faker import Faker
from data_generators.utils import write_generated_data
from repositories.groups_repository import groups_repo

faker = Faker()


def generate_groups(quantity=10):
    groups = []

    for i in range(quantity):
        groups.append({
            '_id': f'{uuid.uuid4()}',
            'name': faker.bothify('??-##', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        })
    write_generated_data(groups_repo, groups)
    return groups
