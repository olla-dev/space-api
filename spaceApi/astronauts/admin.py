from django.contrib import admin

from astronauts.models import Astronaut, AstronautImage, Mission, MissionImage

class AstronautImageAdmin(admin.StackedInline):
    model = AstronautImage

class MissionImageAdmin(admin.StackedInline):
    model = MissionImage

@admin.register(Astronaut)
class AstronautAdmin(admin.ModelAdmin):
    inlines = [AstronautImageAdmin]
    class Meta:
       model = Astronaut

@admin.register(AstronautImage)
class AstronautImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Mission)
class AstronautAdmin(admin.ModelAdmin):
    inlines = [MissionImageAdmin]
    class Meta:
       model = Mission

@admin.register(MissionImage)
class AstronautImageAdmin(admin.ModelAdmin):
    pass
