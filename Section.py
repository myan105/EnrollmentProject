import mongoengine
from mongoengine import *

class Section(Document):
    department_abbreviation = StringField(max_length=6, required=True, description="A reference to 'department_abbreviation' in course.")
    course_number = IntField(min_value=100, max_value=699, required=True, description="A reference to 'course_number' found in course.")
    section_number = IntField(required=True, description="Digits that identifies the section that is offered by a class.")
    semester = StringField(choices=['Fall', 'Spring', 'Summer I', 'Summer II', 'Summer III', 'Winter'], required=True, description="The name of the half-year term that section is offered.")
    section_year = IntField(required=True, description="Number that identifies the year a section is taken.")
    building = StringField(choices=['ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET', 'HSCI', 'NUR', 'VEC'], required=True, description="The structure that the section is located in.")
    room = IntField(min_value=1, max_value=999, required=True, description="Number that identifies the location a section takes place in.")
    schedule = StringField(choices=['MW', 'TuTh', 'MWF', 'F', 'S'], required=True, description="The day that a section takes place.")
    start_time = StringField(max_length=10, required=True, description="Identifies the hour and minute a section begins.")
    instructor = StringField(max_length=50, required=True, description="Name of the person teaching the section.")

    meta = {
        'collection': 'sections',
        'indexes': [
            {'fields': ['course_number', 'section_number', 'semester', 'section_year'], 'unique': True},
            {'fields': ['semester', 'section_year', 'building', 'room', 'schedule', 'start_time'], 'unique': True},
            {'fields': ['semester', 'section_year', 'schedule', 'start_time', 'instructor'], 'unique': True}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_section():
    try:
        department_abbreviation = input("Enter the department abbreviation that the section is assigned to--> ")
        course_number = int(input("Enter the course number that the section is assigned to--> "))
        section_number = int(input("Enter the section number--> "))
        semester = input("Enter the semester section is offered--> ")
        section_year = int(input("Enter the year section is offered--> "))
        building = input("Enter the name of the building of the specific section--> ")
        room = int(input("Enter the room number section is held in--> "))
        schedule = input("Enter the day that the section is offered--> ")
        start_time = input("Enter the time that the section starts--> ")
        instructor = input("Enter the name of the instructor teaching the section--> ")

        section = Section(
            department_abbreviation=department_abbreviation,
            course_number=course_number,
            section_number=section_number,
            semester=semester,
            section_year=section_year,
            building=building,
            room=room,
            schedule=schedule,
            start_time=start_time,
            instructor=instructor
        )

        section.save()
        print("Section added successfully!")
    except Exception as e:
        print("An error occurred:", e)

def list_sections():
    sections = Section.objects().order_by('section_number')
    for section in sections:
        print(section)

def select_section():
    try:
        department_abbreviation = input("Enter the department abbreviation that the section is assigned to--> ")
        course_number = int(input("Enter the course number that the section is assigned to--> "))
        section_number = int(input("Enter the section number--> "))
        semester = input("Enter the semester section is offered--> ")
        section_year = int(input("Enter the year section is offered--> "))

        section = Section.objects(department_abbreviation=department_abbreviation, 
                                  course_number=course_number, 
                                  section_number=section_number, 
                                  semester=semester, 
                                  section_year=section_year).first()
        if section:
            print("Section found:")
            print(section)
        else:
            print("Section not found.")
    except Exception as e:
        print("An error occurred:", e)

def delete_section():
    try:
        department_abbreviation = input("Enter the department abbreviation that the section is assigned to--> ")
        course_number = int(input("Enter the course number that the section is assigned to--> "))
        section_number = int(input("Enter the section number--> "))
        semester = input("Enter the semester section is offered--> ")
        section_year = int(input("Enter the year section is offered--> "))

        section = Section.objects(department_abbreviation=department_abbreviation, 
                                  course_number=course_number, 
                                  section_number=section_number, 
                                  semester=semester, 
                                  section_year=section_year).first()
        if section:
            section.delete()
            print("Section deleted successfully!")
        else:
            print("Section not found.")
    except ValueError:
        print("Invalid input. Please enter valid integers for course number, section number, and section year.")
    except Exception as e:
        print("An error occurred:", e)