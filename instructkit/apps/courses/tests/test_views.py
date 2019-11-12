import json
from unittest import skip

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from accounts.factories import InstructorFactory, StudentFactory
from accounts.models import Student, Instructor
from core.utils import LogMuterTestMixin

from courses.factories import CourseFactory, UnitFactory, LessonFactory, AssignmentFactory


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

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = CourseFactory()
        self.apiclient = APIClient()
        # TODO: Issue #1 - https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
        self.students = [s.id for s in Student.objects.all()]
        self.instructors = [i.id for i in Instructor.objects.all()]

    def test_create_course_success(self):
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
    # TODO: Missing tests: create unit, edit, delete, archive

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = UnitFactory()
        self.apiclient = APIClient()

    @skip('Test isnt creating the course in DB')
    def test_create_unit_success(self):
        url = reverse(self.LIST_URL)
        course = CourseFactory()
        # FIXME: The test doesnt see the course in the test db. Not sure why ...
        unit = {
            'title': 'Programming I',
            'description': 'A test module!',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
            'course': '3be19a27-0d45-4c64-be1e-c72328315d3c',
            'level': 'normal'
        }
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.post(url, json.dumps(unit),
                                       content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)


class LessonAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:lessons'
    DETAIL_URL = 'api:courses:lesson_detail'
    # TODO: Missing tests: create lesson, edit, delete, archive

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = LessonFactory()
        self.apiclient = APIClient()


class AssignmentAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:assignments'
    DETAIL_URL = 'api:courses:assignment_detail'
    # TODO: Missing tests: create assignment, is_complete, edit, delete, archive

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = AssignmentFactory()
        self.apiclient = APIClient()
