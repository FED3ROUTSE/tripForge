from django.db import models

# Create your models here.

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    date_arrival = models.DateField()
    date_departure = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.destination} ({self.date_arrival} - {self.date_departure})"


class Activity(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, help_text="Duration in minutes")

    def __str__(self):
        return self.name
