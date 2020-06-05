from rest_framework.serializers import ModelSerializer
from ..models import Key, Video


class KeySerializer(ModelSerializer):
    """Provide data serialization for `Key` model"""
    class Meta:
        model = Key
        fields = ('id', 'word',)

    def create(self, validated_data):
        """Provide creation of Key with current user"""
        request = self.context['request']

        user = request.user
        validated_data.update(user=user)
        new_key = super().create(validated_data)
        return new_key


class VideoSerializer(ModelSerializer):
    """Provide data serialization for `Video` model"""

    class Meta:
        model = Video
        fields = ('id', 'url')


class KeyWithVideosSerializer(ModelSerializer):
    """Provide data serialization for `Key` model with nested `Video` model"""
    videos = VideoSerializer(many=True)

    class Meta:
        model = Key
        fields = ('id', 'word', 'videos')
