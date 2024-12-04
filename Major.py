import mongoengine
from Department import *

class Major(mongoengine.Document):
    department_abbreviation = mongoengine.StringField(required=True)
    name = mongoengine.StringField(required=True, max_length=50)
    description = mongoengine.StringField(required=True, max_length=80)

    meta = {
        'collection': 'majors',
        'indexes': [
            {'fields': ['name'], 'unique': True},
        ],
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_major():
    success = False
    while not success:
        try:
            department = select_department()
            name = input("Name of major --> ")
            description = input("Description of major --> ")

            major = Major(
                department_abbreviation=department.abbreviation,
                name=name,
                description=description,
            )
            major.save()

            department.update(push__majors=major)
            success = True
        except mongoengine.NotUniqueError:
            print("Major name must be unique. Please try again.")
        except Exception as e:
            print("An error occurred:", e)
            print("Make sure the information is valid.")

def list_major():
    majors = Major.objects().order_by('name')
    for major in majors:
        print(major.name)

def select_major():
    found = False
    while not found:
        major_name = input("Enter the name of the major--> ")
        try:
            major = Major.objects.get(name=major_name)
            found = True
            return major
        except Major.DoesNotExist:
            print("No major with that name. Try again.")

def delete_major():
    major = select_major()
    department = Department.objects.get(abbreviation=major.department_abbreviation)

    department.update(pull__majors=major)
    major.delete()
    print(f"We just deleted the major: {major.name}.")