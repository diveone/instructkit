import datetime as dt
from faker import Faker

from django.core.management.base import BaseCommand
from accounts.models import Instructor, Student
from courses.models import *

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the project with data for demos only.'

    def add_arguments(self, parser):
        # parser.add_argument('csv')
        parser.add_argument('--amount', dest='amount', default=15, type=int)

    def handle(self, *args, **options):
        print("Seeding database ...\n\n")

        print("\tCreating course...")
        for i in range(4):
            course = Course(title="Software Development I",
                            description=fake.sentence(),
                            start=dt.datetime(2019, i+1, 1, hour=9, minute=0),
                            end=dt.datetime(2019, i+6, 1, hour=6, minute=0))
            course.save()

            instructor1 = instructor_factory()
            instructor2 = instructor_factory()
            course.instructors.add(instructor1)
            course.instructors.add(instructor2)

            for _ in range(15):
                student = student_factory()
                course.students.add(student)

            course.save()
            print(f"\tCourse {i} students created {course.students.count()}")
            print(f"\tCourse {i} instructors created: {course.instructors.count()}")


def student_factory():
    student = Student(name=fake.name(), email=fake.email(), github=fake.url(),
                      username=fake.user_name(), website=fake.url(), linkedin=fake.url(),
                      outcome='full-time work', outcome_status='on track')
    student.save()
    return student


def instructor_factory():
    instructor = Instructor(name=fake.name(), email=fake.email(),
                            github=fake.url(), username=fake.user_name(),
                            website=fake.url(), linkedin=fake.url(),
                            speciality='full stack')
    instructor.save()
    return instructor
