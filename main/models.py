from django.db import models


class EventsModel(models.Model):
    event_name = models.CharField(max_length=50)
    event_location = models.CharField(max_length=100)
    event_cost = models.IntegerField()
    event_time = models.DateField()

    def __str__(self):
        return "Event::"+self.event_name