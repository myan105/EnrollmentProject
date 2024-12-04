import mongoengine
from mongoengine import *

class Student(Document):
    lastname = StringField(max_length=50, required=True, description="Last part of what a student is referred as.")
    firstname = StringField(max_length=50, required=True, description="First part of what a student is referred as.")
    eMail = EmailField(max_length=80, required=True, description="An online messaging platform.")

    meta = {
        'collection': 'students',
        'indexes': [
            {'fields': ['lastname', 'firstname'], 'unique': True},
            {'fields': ['eMail'], 'unique': True}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_student():
    try:
        lastname = input("Last name of student--> ")
        firstname = input("First name of student --> ")
        email = input("Enter the email of student --> ")

        student = Student(
            lastname=lastname,
            firstname=firstname,
            eMail=email
        )
        student.save()
        print("Student added successfully!")
    except Exception as e:
        print("An error occurred:", e)

def list_student():
    students = Student.objects().order_by('_id')
    for student in students:
        print(student)

def select_student():
    found = False
    while not found:
        lastname = input("Enter the student's last name --> ")
        firstname = input("Enter the student's first name --> ")
        student = Student.objects(lastname=lastname, firstname=firstname).first()
        found = student is not None
        if not found:
            print("No student with that name. Try again.")
    return student

def delete_student():
    try:
        student = select_student()
        if student:
            student.delete()
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    except Exception as e:
        print("An error occurred:", e)