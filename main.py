import getpass
import certifi
from mongoengine import connect
from Department import Department
from Course import Course
from Section import Section
from Major import Major
from Student import Student
from Enrollment import Enrollment
from Student_Major import StudentMajor
from LetterGrade import LetterGrade
from PassFail import PassFail
from menu_definitions import menu_main, add_menu, delete_menu, list_menu

def add():
    """
    Present the add menu and execute the user's selection.
    """
    add_action = ''
    while add_action != add_menu.last_action():
        add_action = add_menu.menu_prompt()
        exec(add_action)

def delete():
    """
    Present the delete menu and execute the user's selection.
    """
    delete_action = ''
    while delete_action != delete_menu.last_action():
        delete_action = delete_menu.menu_prompt()
        exec(delete_action)

def list_objects():
    """
    Present the list menu and execute the user's selection.
    """
    list_action = ''
    while list_action != list_menu.last_action():
        list_action = list_menu.menu_prompt()
        exec(list_action)

if __name__ == '__main__':
    password = getpass.getpass(prompt="Enter your MongoDB password: ")
    username = "myan105"
    cluster = f"mongodb+srv://anhanson01:hello@singlecollection.eapexrp.mongodb.net/"
try:
    # Connect to MongoDB
    connect(host=cluster, tlsCAFile=certifi.where())

    # Load models to ensure indexes are created
    Department.load_models()
    Course.load_models()
    Section.load_models()
    Major.load_models()
    Student.load_models()
    Enrollment.load_models()
    StudentMajor.load_models()
    LetterGrade.load_models()
    PassFail.load_models()

    while True:
        main_action = menu_main.menu_prompt()
        if main_action == menu_main.last_action():
            break
        elif main_action == add_menu.last_action():
            add()
        elif main_action == delete_menu.last_action():
            delete()
        elif main_action == list_menu.last_action():
            list_objects()

except Exception as e:
    print("An error occurred:", e)