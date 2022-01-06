from django.shortcuts import render
from .models import Astronaut, Mission
from .serializers import AstronautSerializer, MissionSerializer
from rest_framework import viewsets

class AstronautViewSet(viewsets.ModelViewSet):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer
    http_method_names = ['get']

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    http_method_names = ['get']

def index(request):
    return render(request, 'index.html')