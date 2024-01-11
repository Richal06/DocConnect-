# myapp/models.py
from django.db import models

class HeartRate(models.Model):
    rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class HeartRateData(models.Model):
    heart_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Heart Rate: {self.heart_rate} bpm at {self.timestamp}"

