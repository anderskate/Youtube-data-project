from rest_framework import viewsets
from ..models import Key
from .serializers import KeySerializer, KeyWithVideosSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from rest_framework.decorators import action


class KeyViewSet(viewsets.ModelViewSet):
    """View for `Key` model"""
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Override queryset for return only current user's keys"""
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """Create new Key object"""
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                data={'detail': 'Key with this word already exists'},
                status=HTTP_400_BAD_REQUEST,
            )

    @action(methods=['GET'], detail=True)
    def videos(self, request, pk=None):
        """Get all videos for current key."""
        obj = Key.objects.get(id=pk)
        serializer = KeyWithVideosSerializer(
            obj,
            context={'request': request},
        )
        data = serializer.data

        return Response(
            data,
            status=HTTP_200_OK,
        )
