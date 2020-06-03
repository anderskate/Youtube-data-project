from django.test import TestCase
from ..models import Key


class KeyModelTest(TestCase):
    """Test Key Model."""

    def test_saving_and_retrieving_key(self):
        """Check that Key can save and get."""

        first_key = Key()
        first_key.word = 'Auto'
        first_key.save()

        second_key = Key()
        second_key.word = 'Food'
        second_key.save()

        saved_keys = Key.objects.all()
        self.assertEqual(saved_keys.count(), 2)

        first_saved_key = saved_keys[0]
        second_saved_key = saved_keys[1]

        self.assertEqual(first_saved_key.word, 'Auto')
        self.assertEqual(second_saved_key.word, 'Food')

