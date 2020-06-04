from rest_framework import viewsets
from ..models import Key
from .serializers import KeySerializer
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)


class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                data={'detail': 'Key with this word already exists'},
                status=HTTP_400_BAD_REQUEST,
            )
