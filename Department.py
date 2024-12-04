import mongoengine
from mongoengine import *

class Department(Document):
    name = StringField(min_length=10, max_length=50, required=True, description="What the department is called.")
    abbreviation = StringField(max_length=6, required=True, description="An acronym for the specified department.")
    chair_name = StringField(max_length=80, required=True, description="Name of the person in charge of the department.")
    building = StringField(choices=['ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET', 'HSCI', 'NUR', 'VEC'], required=True, description="The structure that the department is located in.")
    office = IntField(required=True, description="The room number that department's chair is located in.")
    description = StringField(max_length=80, required=True, description="A text that explains the department.")
    courses = ListField(ReferenceField('Course'))
    majors = ListField(ReferenceField('Major'))

    meta = {
        'collection': 'departments',
        'indexes': [
            {'fields': ['name'], 'unique': True},
            {'fields': ['abbreviation'], 'unique': True},
            {'fields': ['chair_name'], 'unique': True},
            {'fields': ['building', 'office'], 'unique': True}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()

def add_department():
    try:
        name = input("Department name--> ")
        abbreviation = input("Department abbreviation--> ")
        chair_name = input("Chair name--> ")
        building = input("Building --> ")
        office = int(input("Office number --> "))
        description = input("Description of department --> ")

        department = Department(
            name=name,
            abbreviation=abbreviation,
            chair_name=chair_name,
            building=building,
            office=office,
            description=description
        )
        department.save()
        print("Department added successfully!")
    except Exception as e:
        print("An error occurred:", e)

def list_department():
    departments = Department.objects().order_by('name')
    for department in departments:
        print(f"Name: {department.name}, Abbreviation: {department.abbreviation}, Chair: {department.chair_name}, Building: {department.building}, Office: {department.office}, Description: {department.description}")

def select_department():
    found = False
    while not found:
        abbreviation = input("Enter the department abbreviation--> ")
        department = Department.objects(abbreviation=abbreviation).first()
        found = department is not None
        if not found:
            print("No department with that abbreviation. Try again.")
    return department

def delete_department():
    department = select_department()
    if department:
        if department.courses:
            print("Can't delete this department because it has connected courses.")
        elif department.majors:
            print("Can't delete this department because it has connected majors.")
        else:
            try:
                department.delete()
                print("Department deleted successfully!")
            except Exception as e:
                print("An error occurred:", e)
    else:
        print("Department not found.")