from django.db import models
from django.db.models.fields import DateField, DurationField
from django_countries.fields import CountryField

class Astronaut(models.Model):
    name = models.CharField(max_length=255, default="")
    brief = models.TextField(blank=False, default="")
    birthdate = models.CharField(max_length=255, blank=True, null=True)
    death = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField(multiple=True)
    active_duty = models.BooleanField(default=False, null=True)
    time_in_space = models.CharField(max_length=255, blank=True, null=True)
    total_evas = models.IntegerField(default=0)
    total_eva_time = models.CharField(max_length=255, blank=True, null=True)
    retirement_date = models.DateField(blank=True, null=True)
    wikipedia_url = models.URLField(null=False)
    photo = models.ImageField(upload_to="astronauts/", blank=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
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
    name = models.CharField(max_length=255, default="")
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

    def __str__(self):
        return self.name

class MissionImage(models.Model):
    mission = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.mission.name
