import mongoengine
from mongoengine import *

from Department import *

class Course(Document):
    department_abbreviation = StringField(max_length=6, required=True, description="A reference to abbreviation from department.")
    course_number = IntField(min_value=100, max_value=699, required=True, description="Digits that identifies the class offered by a department.")
    course_name = StringField(max_length=50, required=True, description="What the class is called.")
    units = IntField(min_value=1, max_value=5, required=True, description="Number of credits a course offers.")
    description = StringField(max_length=80, required=True, description="A text that explains the course.")
    sections = ListField(ReferenceField('Section'))

    meta = {
        'collection': 'courses',
        'indexes': [
            {'fields': ['department_abbreviation', 'course_number'], 'unique': True},
            {'fields': ['department_abbreviation', 'course_name'], 'unique': True}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_course():
    try:
        department = select_department()
        course_number = int(input("Course number--> "))
        course_name = input("Course name--> ")
        units = int(input("Units offered--> "))
        description = input("Description of course --> ")

        course = Course(
            department_abbreviation=department.abbreviation,
            course_number=course_number,
            course_name=course_name,
            units=units,
            description=description
        )
        course.save()

        department.update(push__courses=course)
        print("Course added successfully!")
    except Exception as e:
        print("An error occurred:", e)

def list_course():
    courses = Course.objects().order_by('course_number')
    for course in courses:
        print(f"Department Abbreviation: {course.department_abbreviation}, Course Number: {course.course_number}, Course Name: {course.course_name}, Units: {course.units}, Description: {course.description}")

def select_course():
    found = False
    while not found:
        department_abbreviation = input("Enter the department abbreviation the course is connected to--> ")
        course_number = int(input("Enter the course number--> "))
        course = Course.objects(department_abbreviation=department_abbreviation, course_number=course_number).first()
        found = course is not None
        if not found:
            print("No course with that number. Try again.")
    return course

def delete_course():
    course = select_course()
    if course:
        if course.sections:
            print("Can't delete this course because it has connected sections.")
        else:
            try:
                course.delete()
                print("Course deleted successfully!")
            except Exception as e:
                print("An error occurred:", e)
    else:
        print("Course not found.")