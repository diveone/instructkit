import json

from django.test import TestCase
from django.urls import reverse

from .factories import StudentFactory


class StudentAPIViewsTestCase(TestCase):
    def setUp(self):
        self.student = StudentFactory()

    def test_get_students_list(self):
        url = reverse('api:users:students')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_student_detail(self):
        url = reverse('api:users:student_detail', args=[self.student.uid])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        url = reverse('api:users:students')
        user = {
            'username': 'Coltest',
            'email': 'coltest@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(user['username'], response.data['username'])

    def test_edit_student(self):
        url = reverse('api:users:student_detail', args=[self.student.uid])
        updated = {
            'email': 'misstesty@example.com'
        }

        self.client.force_login(self.student)
        response = self.client.patch(url, json.dumps(updated),
                                     content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], 'misstesty@example.com')
