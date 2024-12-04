
from mongoengine import *
from ConstraintUtilities import *
from pprint import pprint
from Student import Student
from Section import Section

class Enrollment(Document):
    student = ReferenceField(Student, db_field='student', required=True)
    section = ReferenceField(Section, db_field='section', required=True)
    semester = StringField(db_field='semester', required=True)
    section_year = StringField(db_field='section_year', required=True)
    department_abbreviation = StringField(db_field='department_abbreviation', required=True)
    course_number = StringField(db_field='course_number', required=True)

    meta = {
        'collection': 'enrollments',
        'indexes': [
            {'unique': True, 'fields': ['student', 'section']},
            {'unique': False, 'fields': ['semester', 'section_year', 'department_abbreviation', 'course_number']}
        ]
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def list_enrollment():
    enrollments = Enrollment.objects().order_by('student')
    for enrollment in enrollments:
        print(f"Student: {enrollment.student}, Section: {enrollment.section}, Semester: {enrollment.semester}, Section Year: {enrollment.section_year}, Department Abbreviation: {enrollment.department_abbreviation}, Course Number: {enrollment.course_number}")

def select_enrollment():
    found = False
    while not found:
        student = select_student()
        section = select_section()
        enrollment = Enrollment.objects(student=student, section=section).first()
        found = enrollment is not None
        if not found:
            print("No enrollment with that student and section was found. Try again.")
    return enrollment


def add_student_section():
    success: bool = False
    while True:
        if success:
            break

        try:
            student = select_student()
            section = select_section()

            enrollment = Enrollment(student='student',section='section')
            enrollment.save()
            print("Student enrolled successfully!")
            success = True
        except Exception as error_message:
            print("The following error occurred:", error_message)
            print("Make sure the information is valid")


def add_section_student():
    success: bool = False

    while True:
        if success:
            break

        try:
            section = select_section()
            student = select_student()

            enrollment = Enrollment(student='student',section='section')
            enrollment.save()

            success = True
        except Exception as error_message:
            print("The following error occurred:", error_message)
            print("Make sure the information is valid")


def list_enrollment():
    enrollments = Enrollment.objects.all().order_by('student')
    for enrollment in enrollments:
        pprint(enrollment)


def select_enrollment():
    found = False

    while not found:
        student = select_student()
        section = select_section()
        enrollments = Enrollment.objects(student='student',section='section').first()
        found = enrollments is not None
        if not found:
            print("No enrollment with that student and section was found.  Try again.")
    return enrollments


def delete_student_section():
    student = select_student()
    section = select_section()
    enrollments = Enrollment.objects(student='student',section='section').first()
    if enrollments:
        enrollments.delete()
        #letter_grades.object(student='student').delete()
        #pass_fails.object(student='student').delete()
        print(f"We just un-enrolled: {enrollments.delete()} student.") ####fix this
    else:
        print("No enrollment found to delete.")


def delete_section_student():
    section = select_section()
    student = select_student()
    enrollments = Enrollment.objects(student='student', sections='section').first
    if enrollments:
        enrollments.delete()
        print(f"We just un-enrolled: {enrollments.delete()} section.")
    else:
        print("No enrollment found to delete.")