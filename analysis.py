import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from repositories.groups_repository import groups_repo
from repositories.subjects_repository import subjects_repo
from repositories.students_repository import students_repo
from repositories.marks_repository import marks_repo

graphics_folder_path = 'plots/'


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
    try:
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
    except Exception as e:
        print(e)


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


def save_figure(image_name, create_figure=None, plot=None):
    fig = plt.figure() if plot is None else plot.get_figure()
    if create_figure is not None:
        create_figure()
    fig.savefig(graphics_folder_path + image_name + '.png', dpi=fig.dpi)

