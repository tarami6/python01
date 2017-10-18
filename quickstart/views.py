from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from tutorial.quickstart.serializer import UserSerializer, GroupSerializer

class UserViuwSet(viewsets.ModelViewSet):
    """
    API endpoint that allows 
    """