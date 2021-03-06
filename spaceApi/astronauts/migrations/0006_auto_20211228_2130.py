# Generated by Django 3.2.7 on 2021-12-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0005_auto_20211228_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronaut',
            name='birthdate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='astronaut',
            name='death',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='astronaut',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
