# Generated by Django 4.0.5 on 2022-07-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0005_summersummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='lck_data',
            name='set',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
