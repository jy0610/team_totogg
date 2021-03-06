# Generated by Django 4.0.5 on 2022-06-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='opggData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(default='', max_length=50, null=True)),
                ('playerName', models.CharField(default='', max_length=50, null=True)),
                ('rst', models.CharField(max_length=20)),
                ('champ_img', models.CharField(default='', max_length=200, null=True)),
                ('champ', models.CharField(max_length=50)),
                ('kda', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
                ('ka', models.CharField(max_length=100)),
                ('cs', models.CharField(max_length=100)),
                ('g_time', models.CharField(max_length=100)),
            ],
        ),
    ]
