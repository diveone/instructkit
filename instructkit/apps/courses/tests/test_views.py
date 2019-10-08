import datetime
import json
from unittest import skip

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from accounts.factories import InstructorFactory, StudentFactory
from accounts.models import Student, Instructor
from core.utils import LogMuterTestMixin

from courses.factories import CourseFactory, UnitFactory
from courses.models import Unit


class CourseLogMuterMixin(LogMuterTestMixin):
    log_names = ['courses.views']


class CourseAPIViewsTestMixin:
    """
    Tests all common API between: Course, Unit, Lesson, Assignment

    A 'module' in this test suite can refer to any of the objects derived from :class `BaseModule``
    """
    VIEW = None
    DETAIL_URL = None
    LIST_URL = None
    USER_FACTORY = None

    def test_get_module_list(self):
        url = reverse(self.LIST_URL)
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_module_detail(self):
        url = reverse(self.DETAIL_URL, args=[self.instance.uid])
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course_fail_unauthenticated_user(self):
        url = reverse(self.LIST_URL)
        response = self.apiclient.post(url, json.dumps({}),
                                       content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def test_create_course_fail_unauthorized_user(self):
        url = reverse(self.LIST_URL)
        response = self.apiclient.post(url, json.dumps({}),
                                       content_type='application/json')
        self.apiclient.force_authenticate(user=self.student)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)


class CourseAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:courses'
    DETAIL_URL = 'api:courses:course_detail'
    MODULE_FACTORY = CourseFactory
    INSTRUCTOR_FACTORY = InstructorFactory
    USER_FACTORY = StudentFactory

    def setUp(self) -> None:
        self.admin = self.INSTRUCTOR_FACTORY(is_superuser=True, is_staff=True)
        self.student = self.USER_FACTORY(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        self.INSTRUCTOR_FACTORY(username='Ms. Han')
        self.instance = self.MODULE_FACTORY()
        self.apiclient = APIClient()
        # TODO: Issue #1 - https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
        self.students = [s.id for s in Student.objects.all()]
        self.instructors = [i.id for i in Instructor.objects.all()]

    def test_create_course(self):
        url = reverse(self.LIST_URL)
        module = {
            'title': 'Programming I',
            'description': 'A test module!',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
            'students': self.students,
            'instructors': self.instructors
        }

        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.post(url, json.dumps(module),
                                       content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_create_course_fail_missing_required_fields(self):
        url = reverse(self.LIST_URL)
        module = {
            'title': 'Programming I',
            'description': 'A test module!',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00'
        }

        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.post(url, json.dumps(module),
                                       content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)


class UnitAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:units'
    DETAIL_URL = 'api:courses:unit_detail'
    MODULE = Unit
    INSTRUCTOR_FACTORY = InstructorFactory
    USER_FACTORY = StudentFactory

    def setUp(self) -> None:
        self.admin = self.INSTRUCTOR_FACTORY(is_superuser=True, is_staff=True)
        self.student = self.USER_FACTORY(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        self.INSTRUCTOR_FACTORY(username='Ms. Han')
        self.instance = UnitFactory()
        self.apiclient = APIClient()
