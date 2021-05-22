from repositories.students_repository import students_repo
from repositories.marks_repository import marks_repo
from repositories.groups_repository import groups_repo
from repositories.subjects_repository import subjects_repo
from data_generators.main import generate_all
from database.utils import drop
from CUI import CUI


def main():
    CUI.show()


if __name__ == '__main__':
    main()
