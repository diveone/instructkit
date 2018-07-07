import factory
import shortuuid
from .models import Instructor, Student


class InstructorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Instructor

    uid = factory.LazyFunction(shortuuid.uuid)
    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    uid = factory.LazyFunction(shortuuid.uuid)
    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
