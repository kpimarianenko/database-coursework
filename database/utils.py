from repositories.groups_repository import groups_repo
from repositories.subjects_repository import subjects_repo
from repositories.students_repository import students_repo
from repositories.marks_repository import marks_repo
import json

backup_file_path = 'outputs/backup.json'


def drop():
    groups_repo.drop()
    subjects_repo.drop()
    students_repo.drop()
    marks_repo.drop()


def backup():
    data = {
        'groups': groups_repo.find_all(),
        'subjects': subjects_repo.find_all(),
        'students': students_repo.find_all(),
        'marks': marks_repo.find_all()
    }

    with open(backup_file_path, 'w+') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def restore():
    try:
        with open(backup_file_path, 'r+') as outfile:
            data = json.load(outfile)
            drop()
            groups_repo.insert_all(data['groups'])
            subjects_repo.insert_all(data['subjects'])
            students_repo.insert_all(data['students'])
            marks_repo.insert_all(data['marks'])
    except:
        print('File "backup.json" is not found or damaged\n')
