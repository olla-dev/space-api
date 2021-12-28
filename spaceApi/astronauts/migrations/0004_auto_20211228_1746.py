# Generated by Django 3.2.7 on 2021-12-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0003_auto_20211228_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='operator',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mission',
            name='total_eva_time',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mission',
            name='total_evas',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='distance_traveled',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='duration',
            field=models.CharField(default='', max_length=255),
        ),
    ]