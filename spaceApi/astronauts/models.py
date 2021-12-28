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
    name = models.CharField(max_length=255)
    brief = models.TextField(blank=False, default="")
    photo = models.ImageField(upload_to="missions/", blank=True)
    type = models.CharField(max_length=255, default="")
    cospar_id = models.CharField(max_length=255, default="")
    satcat_no = models.CharField(max_length=255, default="")
    operator = models.CharField(max_length=255, default="")
    duration = models.CharField(max_length=255, default="")
    distance_traveled = models.CharField(max_length=255, default="")
    total_evas = models.CharField(max_length=255, default="")
    total_eva_time = models.CharField(max_length=255, default="")
    start_date = models.CharField(max_length=255, default="")
    end_date = models.CharField(max_length=255, default="")
    launch_site  = models.CharField(max_length=255, default="")
    landing_site = models.CharField(max_length=255, default="")
    wikipedia_url = models.URLField(null=False, default="")

class MissionImage(models.Model):
    mission = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.mission.name
