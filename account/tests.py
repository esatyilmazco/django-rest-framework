from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse


class UserRegistrationTestCase(APITestCase):
    url = reverse("account:register")
    url_login = reverse("token_obtain_pair")

    def test_user_registration(self):

        data = {
            "username": "esatssss",
            "password": "123"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_invalid_password(self):

        data = {
            "username": "esatssss",
            "password": "123"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):

        self.test_user_registration()

        data = {
            "username": "esatssss",
            "password": "123"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_authenticated_registration(self):

        self.test_user_registration()

        self.client.login(username='oguzhantest', password='denemne')
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_user_authenticated_token_registration(self):

        self.test_user_registration()

        data = {
            "username": "esatssss",
            "password": "123"
        }

        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+token)

        response_2 = self.client.get(self.url)
        self.assertEqual(403, response_2.status_code)
