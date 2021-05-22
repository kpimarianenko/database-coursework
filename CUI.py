from data_generators.main import generate_all
from database.utils import drop


class CUI:
    @staticmethod
    def show():
        while True:
            choice = CUI.print_main_menu()
            if choice == 0:
                break

    @staticmethod
    def print_menu(menu, back_button_title='Exit'):
        index = 1
        for key in menu:
            CUI.print_menu_row(index, key)
            index += 1
        CUI.print_menu_row(0, back_button_title)

        try:
            choice = CUI.get_choice()
            index = 1
            throw_error = True
            for key in menu:
                if index == choice:
                    print()
                    menu[key]()
                    throw_error = False
                index += 1
            if throw_error:
                raise Exception()
            return choice
        except:
            print('Incorrect input. Try again.\n')
            CUI.print_menu(menu, back_button_title)

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
            'Generate random data': lambda: generate_all(1, 2, 3, 1),
            'Drop data': lambda: CUI.prompt(drop)
        })
