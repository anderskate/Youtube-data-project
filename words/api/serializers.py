from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import Key, Video
from datetime import datetime


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
        fields = ('id', 'url', 'creation_date')


class KeyWithVideosSerializer(ModelSerializer):
    """Provide data serialization for `Key` model with nested `Video` model"""
    videos = SerializerMethodField()

    def get_videos(self, obj):
        request = self.context['request']
        videos = obj.videos.all()

        date_gte = request.query_params.get('date_gte', None)
        date_lte = request.query_params.get('date_lte', None)
        if date_gte:
            videos = videos.filter(
                creation_date__gte=datetime.strptime(date_gte, '%d.%m.%Y')
            )
        if date_lte:
            videos = videos.filter(
                creation_date__lte=datetime.strptime(date_lte, '%d.%m.%Y')
            )

        return VideoSerializer(videos, many=True).data

    class Meta:
        model = Key
        fields = ('id', 'word', 'videos')
