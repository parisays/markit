# Generated by Django 2.2.6 on 2019-11-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='connected_platforms',
            field=models.CharField(blank=True, choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook')], default=None, max_length=8, null=True),
        ),
    ]
