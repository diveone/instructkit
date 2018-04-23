import factory
import shortuuid
from .models import Instructor, Student


class InstructorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Instructor


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    uid = factory.LazyFunction(shortuuid.uuid)
