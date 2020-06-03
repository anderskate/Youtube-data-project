from rest_framework.serializers import ModelSerializer
from ..models import Key


class KeySerializer(ModelSerializer):
    class Meta:
        model = Key
        fields = ('id', 'word',)

    def create(self, validated_data):
        request = self.context['request']

        user = request.user
        validated_data.update(user=user)
        new_key = super().create(validated_data)
        return new_key
