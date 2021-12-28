from django.db import models
from django.db.models.fields import DateField, DurationField
from django_countries.fields import CountryField

class Astronaut(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.TextField(blank=False, default="")
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    death = models.DateField(auto_now=False, auto_now_add=False, null=True)
    country = CountryField(multiple=True)
    active_duty = models.BooleanField(default=False)
    time_in_space = models.IntegerField(default=0)
    total_evas = models.IntegerField(default=0)
    total_eva_time = models.IntegerField(default=0)
    retirement_date = models.DateField(blank=True)
    wikipedia_url = models.URLField(null=False)
    photo = models.ImageField(upload_to="astronauts/", blank=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    selection = models.CharField(max_length=255, blank=True)
    missions = models.ManyToManyField("Mission")

    def __str__(self):
        return self.name

class AstronautImage(models.Model):
    astronaut = models.ForeignKey(Astronaut, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.astronaut.name

class Mission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    brief = models.TextField(blank=False, default="")
    photo = models.ImageField(upload_to="missions/", blank=True)
    type = models.CharField(max_length=255)
    cospar_id = models.CharField(max_length=255)
    satcat_no = models.CharField(max_length=255)
    duration = models.DurationField()
    distance_traveled = models.IntegerField(default=0)
    total_evas = models.IntegerField(default=0)
    total_eva_time = models.IntegerField(default=0)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    launch_site  = models.CharField(max_length=255)
    landing_site = models.CharField(max_length=255)
    wikipedia_url = models.URLField(null=False, default="")

class MissionImage(models.Model):
    mission = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.mission.name
