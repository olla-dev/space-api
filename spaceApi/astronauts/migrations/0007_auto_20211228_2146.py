# Generated by Django 3.2.7 on 2021-12-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0006_auto_20211228_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronaut',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='astronaut',
            name='active_duty',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
