# Generated by Django 4.0.5 on 2022-07-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LCK_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_num', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=50)),
                ('rst', models.CharField(max_length=20)),
                ('side', models.CharField(max_length=20)),
                ('gtime', models.CharField(max_length=50)),
                ('gold', models.IntegerField(max_length=50)),
                ('tot_dam', models.IntegerField(max_length=50)),
                ('kill', models.IntegerField(max_length=20)),
                ('death', models.IntegerField(max_length=20)),
                ('assist', models.IntegerField(max_length=20)),
                ('tower', models.IntegerField(max_length=20)),
                ('inhibitor', models.IntegerField(max_length=20)),
                ('herald', models.IntegerField(max_length=20)),
                ('dragon', models.IntegerField(max_length=20)),
                ('elder', models.IntegerField(max_length=20)),
                ('baron', models.IntegerField(max_length=20)),
                ('sight', models.IntegerField(max_length=20)),
                ('total_cs', models.IntegerField(max_length=20)),
            ],
        ),
    ]
