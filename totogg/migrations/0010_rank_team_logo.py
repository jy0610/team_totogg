# Generated by Django 4.0.5 on 2022-07-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0009_remove_rank_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='team_logo',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
