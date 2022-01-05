from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Astronaut, Mission

class AstronautSerializer(CountryFieldMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Astronaut
        fields = [
            "name",
            "brief",
            "birthdate",
            "death",
            "country",
            "active_duty",
            "time_in_space",
            "total_evas",
            "total_eva_time",
            "retirement_date",
            "wikipedia_url",
            "photo",
            "occupation",
            "rank",
            "selection",
            "missions",
        ]
        depth = 1

class MissionSerializer(serializers.HyperlinkedModelSerializer):
    astronauts = AstronautSerializer(read_only=True, many=True)
    class Meta:
        model = Mission
        lookup_field = "id"
        fields = [
            "name",
            "brief",
            "photo",
            "type",
            "cospar_id",
            "satcat_no",
            "operator",
            "duration",
            "distance_traveled",
            "total_evas",
            "total_eva_time",
            "start_date",
            "end_date",
            "launch_site",
            "landing_site",
            "wikipedia_url",
            "astronauts"
        ]

