# Generated by Django 3.2.7 on 2021-12-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronauts', '0004_auto_20211228_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='cospar_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='end_date',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='landing_site',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='launch_site',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='satcat_no',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='start_date',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='type',
            field=models.CharField(default='', max_length=255),
        ),
    ]
