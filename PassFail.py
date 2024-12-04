import mongoengine
from Enrollment import *
from datetime import datetime

class PassFail(mongoengine.Document):
    student_id = mongoengine.ReferenceField(Enrollment, required=True)
    application_date = mongoengine.DateTimeField(default=datetime.now)

    meta = {
        'collection': 'pass_fails',
    }

    @classmethod
    def load_models(cls):
        """Ensures indexes are created."""
        cls.ensure_indexes()
def add_student_pass_fail():
    success = False
    while not success:
        try:
            enrollment = select_enrollment()

            pass_fail = PassFail(
                student_id=enrollment,
            )
            pass_fail.save()

            enrollment.pass_fail = datetime.now()
            enrollment.save()

            success = True
        except Exception as e:
            print("An error occurred:", e)
            print("Make sure the information is valid.")
def delete_pass_fail():
    try:
        enrollment = select_enrollment()
        pass_fail = PassFail.objects(student_id=enrollment).first()
        if pass_fail:
            pass_fail.delete()
            print("Pass/Fail record deleted successfully!")
        else:
            print("Pass/Fail record not found.")
    except Exception as e:
        print("An error occurred:", e)

def list_pass_fails():
    pass_fails = PassFail.objects().order_by('application_date')
    for pass_fail in pass_fails:
        print(pass_fail)