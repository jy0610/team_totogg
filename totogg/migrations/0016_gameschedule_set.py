# Generated by Django 4.0.5 on 2022-07-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0015_rename_cs_recentsummary_tot_dam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameschedule',
            name='set',
            field=models.IntegerField(null=True),
        ),
    ]
