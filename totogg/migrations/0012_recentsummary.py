# Generated by Django 4.0.5 on 2022-07-09 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0011_summer_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='recentSummary',
            fields=[
                ('tname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('gold', models.FloatField()),
                ('dam', models.FloatField()),
                ('kill', models.FloatField()),
                ('tower', models.FloatField()),
                ('inhibitor', models.FloatField()),
                ('dragon', models.FloatField()),
                ('baron', models.FloatField()),
                ('cs', models.FloatField()),
            ],
        ),
    ]
