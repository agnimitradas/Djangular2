from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import EventsSerializers
from .models import EventsModel


class EventsView(ModelViewSet):
    queryset = EventsModel.objects.all()
    serializer_class = EventsSerializers
    #token = Token.objects.create(user=User)
    #print(token.key)
    #permission_classes = (permissions.IsAdminUser,)
