from django.shortcuts import render
from rest_framework import status, viewsets
from ..models import Key
from .serializers import KeySerializer
from rest_framework.permissions import IsAuthenticated


class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
