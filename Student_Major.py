import mongoengine
from mongoengine import *

class StudentMajor(Document):
    major_name = StringField(max_length=50, required=True, description="What the major is called.")
    last_name = StringField(max_length=50, required=True, description="Last part of what a student is referred as.")
    first_name = StringField(max_length=50, required=True, description="First part of what a student is referred as.")

    meta = {
        'collection': 'student_majors',
        'indexes': [
            {'fields': ['major_name', 'last_name', 'first_name'], 'unique': True}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_student_major():
    try:
        student = select_student()
        major = select_major()

        student_major = StudentMajor(
            major_name=major.name,
            last_name=student.lastname,
            first_name=student.firstname
        )

        student_major.save()
        print("Student major added successfully!")
    except Exception as e:
        print("An error occurred:", e)

def list_student_major():
    student_majors = StudentMajor.objects().order_by('major_name')
    for student_major in student_majors:
        print(student_major)

def delete_student_major():
    try:
        student = select_student()
        major = select_major()

        student_major = StudentMajor.objects(major_name=major.name,
                                             last_name=student.lastname,
                                             first_name=student.firstname).first()
        if student_major:
            student_major.delete()
            print("Student major deleted successfully!")
        else:
            print("Student major not found.")
    except Exception as e:
        print("An error occurred:", e)

