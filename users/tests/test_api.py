from rest_framework.test import APITestCase
from rest_framework import status
from ..models import User


class TestUser(APITestCase):
    """Test `Users` API
        Test creation and retrieving User information
        """
    order_url = '/api/v1/users/'

    def test_create_new_user(self):
        """Test that user creating is successful."""
        data = {
            'username': 'Test User',
            'email': 'test@mail.ru',
            'password': 'Test123pass',
        }
        response = self.client.post(
            self.order_url,
            data=data,
            format='json',
        )
        new_user = User.objects.get(email=data['email'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_user.username, response.data['username'])
