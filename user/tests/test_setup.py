from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self) -> None:
        self.register_url = reverse('user:register')
        self.login_url = reverse('user:login')
        self.current_user_url = reverse('user:current-user')

        self.register_data = {
            "full_name": "Pawan lal Ganesh",
            "email": "pawanlalganesh@gmail.com",
            "password": "Secret@123"
        }

        self.login_data = {
            "email": "pawanlalganesh@gmail.com",
            "password": "Secret@123"
        }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
