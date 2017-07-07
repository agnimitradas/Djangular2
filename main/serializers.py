from rest_framework import serializers
from .models import EventsModel

class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventsModel
        fields = '__all__'