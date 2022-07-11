# Generated by Django 4.0.5 on 2022-07-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0010_rank_team_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summer_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_num', models.CharField(max_length=20)),
                ('set', models.IntegerField(default=0, null=True)),
                ('team', models.CharField(max_length=50)),
                ('side', models.CharField(max_length=20)),
                ('gtime', models.CharField(max_length=50)),
                ('gold', models.IntegerField()),
                ('tot_dam', models.IntegerField()),
                ('kill', models.IntegerField()),
                ('death', models.IntegerField()),
                ('assist', models.IntegerField()),
                ('tower', models.IntegerField()),
                ('inhibitor', models.IntegerField()),
                ('herald', models.IntegerField()),
                ('dragon', models.IntegerField()),
                ('elder', models.IntegerField()),
                ('baron', models.IntegerField()),
                ('sight', models.IntegerField()),
                ('total_cs', models.IntegerField()),
                ('rst', models.CharField(max_length=20)),
            ],
        ),
    ]
