# Generated by Django 4.0.5 on 2022-07-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lck_data',
            name='assist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='baron',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='death',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='dragon',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='elder',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='gold',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='herald',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='inhibitor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='kill',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='sight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='tot_dam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='total_cs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lck_data',
            name='tower',
            field=models.IntegerField(),
        ),
    ]