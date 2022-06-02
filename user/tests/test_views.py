import pdb
from .test_setup import TestSetup


class TestViews(TestSetup):
    def test_user_registration_request_create_api_view(self):
        response = self.client.post(self.register_url, self.register_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_login_request_api_view(self):
        register_response = self.client.post(self.register_url, self.register_data, format='json')
        self.assertEqual(register_response.status_code, 201)
        login_response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(login_response.status_code, 200)

    def test_user_profile_retrieve_update_api_view_with_valid_token(self):
        register_response = self.client.post(self.register_url, self.register_data, format='json')
        self.assertEqual(register_response.status_code, 201)
        login_response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(login_response.status_code, 200)
        token = login_response.data['access_token']
        response = self.client.get(self.current_user_url, HTTP_AUTHORIZATION='Bearer ' + token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], self.register_data['email'])

    def test_user_profile_retrieve_update_api_view_with_invalid_token(self):
        register_response = self.client.post(self.register_url, self.register_data, format='json')
        self.assertEqual(register_response.status_code, 201)
        login_response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(login_response.status_code, 200)
        token = login_response.data['access_token']
        response = self.client.get(self.current_user_url, HTTP_AUTHORIZATION='Bearer ' + token + 'invalid')
        self.assertEqual(response.status_code, 403)

    def test_user_profile_retrieve_update_api_view_without_token(self):
        response = self.client.get(self.current_user_url)
        self.assertEqual(response.status_code, 403)
