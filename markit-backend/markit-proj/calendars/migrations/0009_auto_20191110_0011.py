# Generated by Django 2.2.6 on 2019-11-09 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0008_auto_20191108_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='twitter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='twitter', to='socialaccount.SocialAccount'),
        ),
    ]
