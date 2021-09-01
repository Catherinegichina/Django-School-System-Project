from django.db import models

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=20)
    event_planner=models.CharField(max_length=20)
    event_agenda=models.CharField(max_length=13)
    # event_duration=models.DateTimeField()
    event_venue=models.CharField(max_length=10)
    event_attendees=models.CharField(max_length=16)