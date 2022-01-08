from rest_framework import serializers
import json
from .models import Astronaut, Mission

class MissionBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Mission
        fields = [
            "id",
            "name",
            "brief",
            "photo",
        ]

class AstronautSerializer(serializers.HyperlinkedModelSerializer):
    missions = MissionBaseSerializer(many=True)
    countries = serializers.SerializerMethodField()

    class Meta:
        model = Astronaut
        lookup_field = "id"
        fields = [
            "id",
            "name",
            "brief",
            "birthdate",
            "death",
            "countries",
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

    def get_countries(self, obj):
        country_list = obj.countries.replace("[", "").replace("]","").split(",")
        return json.loads(json.dumps(country_list))

class AstronautNestedSerializer(AstronautSerializer):
    class Meta:
        model = Astronaut
        fields = [
            "id",
            "name",
            "brief",
            "photo",
            "countries",
        ]


class MissionSerializer(MissionBaseSerializer):
    crew = AstronautNestedSerializer(many=True, read_only=True)
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
            "crew",
        ]

