# Generated by Django 3.2.7 on 2021-12-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0009_alter_astronaut_retirement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronaut',
            name='total_eva_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
