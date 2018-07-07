import json

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .factories import InstructorFactory, StudentFactory


class AccountsAPIViewsTestMixin:
    VIEW = None
    DETAIL_URL = None
    LIST_URL = None
    USER_FACTORY = None

    def test_get_user_list(self):
        url = reverse(self.LIST_URL)
        self.factory.force_authenticate(user=self.admin)
        response = self.factory.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        url = reverse(self.DETAIL_URL, args=[self.user.uid])
        self.factory.force_authenticate(user=self.admin)
        response = self.factory.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse(self.LIST_URL)
        user = {
            'username': 'Coltest',
            'email': 'coltest@example.com',
            'password': 'testpassword'
        }

        self.factory.force_authenticate(user=self.admin)
        response = self.factory.post(url, json.dumps(user),
                                     content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user['username'], response.data['username'])

    def test_create_user_forbidden(self):
        url = reverse(self.LIST_URL)
        user = {
            'email': 'coltest@example.com',
            'password': 'testpassword'
        }
        response = self.factory.post(url, json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_user(self):
        url = reverse(self.DETAIL_URL, args=[self.user.uid])
        updated = {
            'email': 'misstesty@example.com'
        }

        self.factory.force_authenticate(user=self.admin)
        response = self.factory.patch(url, json.dumps(updated),
                                     content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'misstesty@example.com')


class InstructorAPIViewsTestCase(TestCase, AccountsAPIViewsTestMixin):
    LIST_URL = 'api:users:instructors'
    DETAIL_URL = 'api:users:instructor_detail'
    USER_FACTORY = InstructorFactory

    def setUp(self):
        self.user = self.USER_FACTORY()
        self.admin = self.USER_FACTORY(is_superuser=True, is_staff=True)
        self.factory = APIClient()


class StudentAPIViewsTestCase(TestCase, AccountsAPIViewsTestMixin):
    LIST_URL = 'api:users:students'
    DETAIL_URL = 'api:users:student_detail'
    USER_FACTORY = StudentFactory

    def setUp(self):
        self.user = self.USER_FACTORY()
        self.admin = self.USER_FACTORY(is_superuser=True, is_staff=True)
        self.factory = APIClient()
