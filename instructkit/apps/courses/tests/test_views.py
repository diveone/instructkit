import json
import factory
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
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
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

    @skip('TODO - Issue #11: Not implemented')
    def test_archive_module_success(self):
        pass


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
        self.assertEqual(response.data['title'], 'Programming I', response.data)

    def test_create_course_fail_missing_required_fields(self):
        url = reverse(self.LIST_URL)
        module = {
            'title': 'Programming I',
            'description': 'A programming course!',
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

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = UnitFactory()
        self.apiclient = APIClient()

    def test_create_unit_success(self):
        url = reverse(self.LIST_URL)
        course = CourseFactory()
        unit = {
            'title': 'Programming I',
            'description': 'A test module!',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
            'course': str(course.id),
            'level': 'normal'
        }
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.post(url, json.dumps(unit),
                                       content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)

    def test_patch_unit_success(self):
        """PATCH request to update Unit"""
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        update = {
            'title': 'A new Detailed Title'
        }
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.patch(url, json.dumps(update),
                                        content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)

    def test_update_unit_success(self):
        """PUT request to update Unit"""
        course = CourseFactory()
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        data = factory.build(dict, FACTORY_CLASS=UnitFactory)
        data.update({
            'id': str(data['id']),
            'course': str(course.id),
            'start': str(data['start']),
            'end': str(data['end']),
            'title': 'A brand new, totally unique title'
        })
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.put(url, json.dumps(data),
                                      content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)

    def test_delete_unit_success(self):
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.delete(url, content_type='application/json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)


class LessonAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:lessons'
    DETAIL_URL = 'api:courses:lesson_detail'

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = LessonFactory()
        self.apiclient = APIClient()

    def test_create_lesson_success(self):
        url = reverse(self.LIST_URL)
        unit = UnitFactory()
        lesson = {
            'title': 'How to use Lists I',
            'description': 'A lesson on data structures list.',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
            'instructor': str(self.admin.id),
            'unit': str(unit.id)
        }
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.post(url, json.dumps(lesson),
                                       content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)

    def test_patch_lesson_success(self):
        """PATCH request to update lesson."""
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        update = {
            'title': 'How to use Lists II',
        }
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.patch(url, json.dumps(update),
                                        content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)

    def test_update_lesson_success(self):
        """PUT request to update lesson."""
        unit = UnitFactory()
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        data = factory.build(dict, FACTORY_CLASS=LessonFactory)
        data.update({
            'id': str(self.instance.id),
            'title': 'How to use Lists III Update',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
            'unit': str(unit.id),
            'instructor': str(self.admin.id)
        })
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.put(url, json.dumps(data),
                                      content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)

    def test_delete_lesson_success(self):
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        self.apiclient.force_authenticate(user=self.admin)
        response = self.apiclient.delete(url, content_type='application/json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)


class AssignmentAPIViewsTestCase(TestCase, CourseAPIViewsTestMixin, CourseLogMuterMixin):
    LIST_URL = 'api:courses:assignments'
    DETAIL_URL = 'api:courses:assignment_detail'

    def setUp(self) -> None:
        self.admin = InstructorFactory(is_superuser=True, is_staff=True)
        self.student = StudentFactory(username='joan')
        StudentFactory(username='joe')
        StudentFactory(username='jane')
        InstructorFactory(username='Ms. Han')
        self.instance = AssignmentFactory()
        self.apiclient = APIClient()

    def test_create_assignment_success(self):
        url = reverse(self.LIST_URL)
        lesson = LessonFactory()
        # TODO: Issue #12 - Setup Assignment.url so it doesn't require https://
        assignment = {
            'title': 'Homework',
            'description': 'A homework assignment',
            'lesson': str(lesson.id),
            'category': 'homework',
            'url': 'https://homework.example.com',
            'document': 'Some document text.',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
        }

        self.apiclient.force_login(self.admin)
        response = self.apiclient.post(url, json.dumps(assignment),
                                       content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)

    def test_patch_assignment_success(self):
        """PATCH request to update assignment"""
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        update = {
            'title': 'New homework title'
        }
        self.apiclient.force_login(self.admin)
        response = self.apiclient.get(url)
        self.assertEqual(self.instance.title, response.data['title'])

        response = self.apiclient.patch(url, json.dumps(update),
                                        content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEqual('New homework title', response.data['title'], response.data)

    def test_update_assignment_success(self):
        """PUT request to update assignment"""
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        lesson = LessonFactory()
        assignment = {
            'id': str(self.instance.id),
            'title': 'Updated Homework Assignment',
            'description': 'An updated homework assignment',
            'lesson': str(lesson.id),
            'category': 'homework',
            'url': 'https://homework.example.com',
            'document': 'Some document text.',
            'start': '2050-01-01T00:00',
            'end': '2050-04-01T00:00',
        }

        self.apiclient.force_login(self.admin)
        response = self.apiclient.get(url)
        self.assertEqual(self.instance.title, response.data['title'])

        response = self.apiclient.put(url, json.dumps(assignment),
                                      content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEqual('Updated Homework Assignment',
                         response.data['title'],
                         response.data)

    def test_delete_assignment_success(self):
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        self.apiclient.force_login(self.admin)
        response = self.apiclient.delete(url, content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)

    def test_toggle_is_complete_success(self):
        url = reverse(self.DETAIL_URL, args=[self.instance.id])
        update = {
            'is_complete': True
        }
        self.apiclient.force_login(self.admin)
        response = self.apiclient.get(url)
        self.assertFalse(response.data['is_complete'])

        response = self.apiclient.patch(url, json.dumps(update),
                                        content_type='application/json')
        self.assertTrue(response.data['is_complete'], response.data)
