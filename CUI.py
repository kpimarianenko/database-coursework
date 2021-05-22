from data_generators.main import generate_all
from database.utils import drop, backup, restore
import analysis


class CUI:
    @staticmethod
    def show():
        CUI.print_main_menu()

    @staticmethod
    def print_menu(menu, back_button_title='Exit'):
        while True:
            index = 1
            for key in menu:
                CUI.print_menu_row(index, key)
                index += 1
            CUI.print_menu_row(0, back_button_title)

            try:
                choice = CUI.get_choice()
                if choice == 0:
                    print()
                    break

                index = 1
                throw_error = True
                for key in menu:
                    if index == choice:
                        print()
                        menu[key]()
                        throw_error = False
                    index += 1
                if throw_error and choice != 0:
                    raise Exception()
            except:
                print('Incorrect input. Try again.\n')

    @staticmethod
    def print_menu_row(key, title):
        print(f'[{key}]. {title}')

    @staticmethod
    def get_choice(message='Choose your next action: '):
        choice = int(input(message))
        return choice

    @staticmethod
    def prompt(action, message='Are you sure?'):
        choice = input(f'{message} [Y/N]: ').upper()
        print()
        if choice == 'Y':
            return action()
        if choice == 'N':
            return
        return CUI.prompt(action, 'Incorrect input. Try again.')

    @staticmethod
    def print_main_menu():
        return CUI.print_menu({
            'Generate random data': lambda: generate_all(4, 5, 3, 3),
            'Drop data': lambda: CUI.prompt(drop),
            'Create backup': lambda: backup(),
            'Restore database': lambda: CUI.prompt(restore),
            'Data analysis': lambda: CUI.print_analysis_menu()
        })

    @staticmethod
    def print_analysis_menu():
        return CUI.print_menu({
            'Average mark in group': lambda: analysis.create_average_mark_in_group_plot(),
            'Average mark by subject': lambda: analysis.create_average_mark_by_subject_plot(),
            'Average mark in group by each subject': lambda: analysis.create_average_mark_in_group_by_each_subject_plot(),
            'Age mark plot': lambda: analysis.create_age_mark_plot()
        }, 'Back')

