# Generated by Django 4.0 on 2022-01-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0011_mission_crew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='astronaut',
            name='country',
        ),
        migrations.AddField(
            model_name='astronaut',
            name='countries',
            field=models.CharField(default='"[]"', max_length=255),
        ),
    ]
