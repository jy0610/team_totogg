# Generated by Django 4.0.5 on 2022-07-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0002_alter_lck_data_assist_alter_lck_data_baron_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('score_wins', models.CharField(max_length=50)),
                ('score_loses', models.CharField(max_length=50)),
                ('teascore_scd', models.CharField(max_length=50)),
                ('score_wins_rates', models.CharField(max_length=50)),
            ],
        ),
    ]
