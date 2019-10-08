import datetime
import uuid

import factory
from factory.fuzzy import FuzzyNaiveDateTime

from .models import Course, Unit

fdt = FuzzyNaiveDateTime(datetime.datetime(2050, 1, 1), datetime.datetime(2050, 4, 1))


class ModuleMixin:
    uid = factory.LazyFunction(uuid.uuid4)
    start = fdt.start_dt
    end = fdt.end_dt


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    uid = factory.LazyFunction(uuid.uuid4)
    start = fdt.start_dt
    end = fdt.end_dt


class UnitFactory(factory.DjangoModelFactory, ModuleMixin):
    class Meta:
        model = Unit

    uid = factory.LazyFunction(uuid.uuid4)
    course = factory.SubFactory(CourseFactory)
    start = fdt.start_dt
    end = fdt.end_dt
