import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from repositories.groups_repository import groups_repo
from repositories.subjects_repository import subjects_repo
from repositories.students_repository import students_repo
from repositories.marks_repository import marks_repo

graphics_folder_path = 'outputs/plots/'


def create_average_mark_in_group_plot():
    data = {}
    groups = groups_repo.find_all()

    for g in groups:
        group_id = g['_id']
        group_name = g['name']
        group_marks = marks_repo.get_marks_by_group(group_id)
        mean_value = np.mean(list(map(lambda m: m['value'], group_marks)))
        data[group_name] = mean_value

    save_figure('average_mark_in_group', lambda: plt.bar(data.keys(), data.values()))


def create_average_mark_by_subject_plot():
    data = {}
    subjects = subjects_repo.find_all()

    for s in subjects:
        subject_id = s['_id']
        subject_name = s['name']
        subject_marks = marks_repo.find({'subject_id': subject_id})
        mapped_marks = list(map(lambda m: m['value'], subject_marks))
        mean_value = np.mean(mapped_marks) if len(mapped_marks) > 0 else 0
        data[subject_name] = mean_value

    save_figure('average_mark_by_subject', lambda: plt.bar(data.keys(), data.values()))


def create_average_mark_in_group_by_each_subject_plot():
    data = {}
    groups = groups_repo.find_all()
    subjects = subjects_repo.find_all()

    for s in subjects:
        subject_id = s['_id']
        subject_name = s['name']
        values = []
        for g in groups:
            group_id = g['_id']
            marks = marks_repo.get_marks_by_group_and_subject(group_id, subject_id)
            mapped_marks = list(map(lambda m: m['value'], marks))
            mean_value = np.mean(mapped_marks) if len(mapped_marks) > 0 else 0
            values.append(mean_value)
        data[subject_name] = values

    plot = pd.DataFrame(data, index=list(map(lambda m: m['name'], groups))).plot(kind='bar')
    save_figure('average_mark_in_group_by_each_subject', plot=plot)


def create_age_mark_plot():
    data = {}
    ages = students_repo.get_ages()

    for a in ages:
        marks = marks_repo.get_marks_by_student_age(a)
        mapped_marks = list(map(lambda m: m['value'], marks))
        mean_value = np.mean(mapped_marks) if len(mapped_marks) > 0 else 0
        data[a] = mean_value

    save_figure('age_mark_plot', lambda: plt.plot(data.keys(), data.values()))


def create_group_activity_pie_plot():
    data = {}
    groups = groups_repo.find_all()

    for g in groups:
        group_id = g['_id']
        group_name = g['name']
        count = marks_repo.get_group_marks_count(group_id)
        data[group_name] = count

    plt.title('Groups activity')
    plt.axis('equal')

    save_figure('group_activity_pie', lambda: plt.pie(data.values(), labels=data.keys(), shadow=True, autopct='%1.1f%%'))


def save_figure(image_name, create_figure=None, plot=None):
    fig = plt.figure() if plot is None else plot.get_figure()
    if create_figure is not None:
        create_figure()
    fig.savefig(graphics_folder_path + image_name + '.png', dpi=fig.dpi)

