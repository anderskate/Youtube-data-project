from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Key, Video

from users.factories import UserFactory

from datetime import datetime


class TestWordsApi(APITestCase):
    """Test `Search` API
    Test creation, deleting and retrieving Search keys
    """
    order_url = '/api/v1/words/'

    def setUp(self):
        self.user = UserFactory()
        self.different_user = UserFactory()
        self.token = self.get_tokens_for_user(self.user)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)

    def test_requests_without_auth_user(self):
        """Test that you can’t get, delete and create 'words'
        without authorization.
        """
        response1 = self.client.get(self.order_url)

        self.assertEqual(response1.status_code, status.HTTP_401_UNAUTHORIZED)

        response2 = self.client.post(
            self.order_url,
            data={},
        )
        keys = Key.objects.all()

        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(keys.count(), 0)

        new_key = Key.objects.create(word='Test', user=self.user)
        url_for_delete = f'{self.order_url}{new_key.id}/'
        response3 = self.client.delete(
            url_for_delete,
        )

        self.assertEqual(response3.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_key_with_auth_user(self):
        """Test create key with authentication user."""
        data = {'word': 'cars'}

        response = self.client.post(
            self.order_url,
            HTTP_AUTHORIZATION='Bearer ' + self.token,
            data=data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        key = Key.objects.get(id=response.data['id'])
        self.assertEqual(key.word, data.get('word'))

    def test_get_keys_with_auth_user(self):
        """Test get keys with authentication user."""
        Key.objects.create(user=self.user, word='Test1')
        Key.objects.create(user=self.user, word='Test2')

        Key.objects.create(user=self.different_user, word='Test3')

        response = self.client.get(
            self.order_url,
            HTTP_AUTHORIZATION='Bearer ' + self.token,
            format='json',
        )

        keys = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(keys), 2)

    def test_delete_key_with_auth_user(self):
        """Test delete key with authentication user."""
        new_key = Key.objects.create(user=self.user, word='Test1')
        url = f'{self.order_url}{new_key.id}/'
        response = self.client.delete(
            url,
            HTTP_AUTHORIZATION='Bearer ' + self.token,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count_user_keys = Key.objects.count()
        self.assertEqual(count_user_keys, 0)

    def test_get_all_videos_to_word(self):
        """Test that can get all videos for specific word."""
        new_word = Key.objects.create(user=self.user, word='Test1')
        video_1 = Video.objects.create(key=new_word, url='sample1.url')
        video_2 = Video.objects.create(key=new_word, url='sample2.url')

        url = f'{self.order_url}{new_word.id}/videos/'
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION='Bearer ' + self.token,
            format='json',
        )
        videos = response.data.get('videos')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(videos), 2)

    def test_get_videos_with_specific_datetime(self):
        """Test that can get videos with specific datetime."""
        new_word = Key.objects.create(user=self.user, word='Test2')
        video_1 = Video.objects.create(
            key=new_word,
            url='sample1.url',
        )
        video_1.creation_date = datetime(2020, 6, 10)
        video_1.save()
        video_2 = Video.objects.create(
            key=new_word,
            url='sample2.url',
            creation_date=datetime(2020, 6, 10)
        )
        video_2.creation_date = datetime(2020, 6, 10)
        video_2.save()
        video_without_correct_date = Video.objects.create(
            key=new_word,
            url='sample2.url',
        )
        start_time = '09.06.2020'
        close_time = '13.06.2020'

        url = f'{self.order_url}{new_word.id}/videos/'\
              f'?date_gte={start_time}&date_lte={close_time}'
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION='Bearer ' + self.token,
            format='json',
        )
        videos = response.data.get('videos')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(videos), 2)
        self.assertContains(response, 'sample1.url')
        self.assertContains(response, 'sample2.url')
