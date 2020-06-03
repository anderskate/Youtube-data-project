from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User Model"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create a new User"""
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
