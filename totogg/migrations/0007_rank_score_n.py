# Generated by Django 4.0.5 on 2022-07-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0006_lck_data_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='score_n',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
