from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Key


class TestWorldsApi(APITestCase):
    """Test `Search` API
    Test creation, deleting and retrieving Search keys
    """
    order_url = '/api/v1/words/'

    def test_requests_with_not_auth_user(self):
        pass

    def test_create_key_with_auth_user(self):
        data = {'word': 'cars'}

        response = self.client.post(
            self.order_url,
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        key = Key.objects.get(id=response.data['id'])
        self.assertEqual(key.word, data.get('word'))

    def test_get_keys_with_auth_user(self):
        key1 = Key.objects.create()
        key2 = Key.objects.create()

        response = self.client.get(
            self.order_url
        )

    def test_delete_key_with_auth_user(self):
        pass
