import factory
import uuid
from .models import User


class UserFactory(factory.DjangoModelFactory):
    """Factory for generates test `User` model"""
    username = factory.Faker('name')

    @factory.lazy_attribute
    def email(self):
        return f'{uuid.uuid4()}@mail.ru'

    @factory.lazy_attribute
    def password(self):
        return f'{uuid.uuid4()}'

    class Meta:
        model = User
