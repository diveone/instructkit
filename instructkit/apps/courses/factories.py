import datetime
import uuid

import factory
from factory.fuzzy import FuzzyNaiveDateTime, FuzzyChoice, FuzzyText

from accounts.factories import InstructorFactory
from .models import Course, Unit, Lesson, Assignment

fdt = FuzzyNaiveDateTime(datetime.datetime(2050, 1, 1), datetime.datetime(2050, 4, 1))


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    id = factory.LazyFunction(uuid.uuid4)
    start = fdt.start_dt
    end = fdt.end_dt


class UnitFactory(factory.DjangoModelFactory):
    class Meta:
        model = Unit

    id = factory.LazyFunction(uuid.uuid4)
    course = factory.SubFactory(CourseFactory)
    description = FuzzyText()
    level = FuzzyChoice(['low', 'normal', 'medium', 'high'])
    start = fdt.start_dt
    end = fdt.end_dt


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson

    id = factory.LazyFunction(uuid.uuid4)
    description = FuzzyText()
    unit = factory.SubFactory(UnitFactory)
    instructor = factory.SubFactory(InstructorFactory)
    start = fdt.start_dt
    end = fdt.end_dt


class AssignmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Assignment

    id = factory.LazyFunction(uuid.uuid4)
    lesson = factory.SubFactory(LessonFactory)
    category = FuzzyChoice(['homework', 'project', 'exercise'])
    url = 'assignment.example.com'
    document = FuzzyText(length=500)
    is_complete = False
    start = fdt.start_dt
    end = fdt.end_dt
