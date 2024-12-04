from mongoengine import Document, StringField, ReferenceField
from Enrollment import Enrollment

class LetterGrade(Document):
    student_id = ReferenceField("Enrollment", required=True)
    min_satisfactory = StringField(required=True, choices=['A', 'B', 'C'])

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()

def add_letter_grade():
    success = False

    while not success:
        try:
            enrollment = select_enrollment()

            min_satisfactory = input("Select the minimum letter grade ('A', 'B', 'C'): ")
            while min_satisfactory not in ['A', 'B', 'C']:
                min_satisfactory = input("The minimum grade must be a valid grade ('A', 'B', 'C'): ")

            letter_grade = LetterGrade(student_id=enrollment, min_satisfactory=min_satisfactory)
            letter_grade.save()

            enrollment.letter_grade = min_satisfactory
            enrollment.save()

            print("Letter grade added successfully!")
            success = True
        except Exception as error_message:
            print("The following error occurred:", error_message)
            print("Make sure the information is valid")
def delete_letter_grade():
    try:
        student_id = input("Enter student ID for whom you want to delete the letter grade: ")
        letter_grade = LetterGrade.objects(student_id=student_id).first()
        if letter_grade:
            letter_grade.delete()
            print("Letter grade deleted successfully!")
        else:
            print("No letter grade found for the given student ID.")
    except Exception as e:
        print("An error occurred:", e)

def list_letter_grades():
    try:
        letter_grades = LetterGrade.objects().order_by('student_id')
        if letter_grades:
            print("Letter grades:")
            for letter_grade in letter_grades:
                print(f"Student ID: {letter_grade.student_id}, Minimum Satisfactory: {letter_grade.min_satisfactory}")
        else:
            print("No letter grades found.")
    except Exception as e:
        print("An error occurred:", e)
