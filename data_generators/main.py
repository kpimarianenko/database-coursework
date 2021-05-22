from data_generators.groups_generator import generate_groups
from data_generators.subjects_generator import generate_subjects
from data_generators.students_generator import generate_students
from data_generators.marks_generator import generate_marks
import random


def generate_all(groups_quantity, subjects_quantity, students_in_groups_quantity, student_marks_quantity):
    groups = generate_groups(groups_quantity)
    subjects = generate_subjects(subjects_quantity)

    for g in groups:
        students = generate_students(g['_id'], students_in_groups_quantity)
        for s in students:
            subject_id = random.choice(subjects)['_id']
            generate_marks(s['_id'], subject_id, student_marks_quantity)
