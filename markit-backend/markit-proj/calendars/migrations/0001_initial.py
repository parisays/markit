# Generated by Django 2.2.6 on 2019-11-25 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('connectedPlatforms', models.CharField(blank=True, choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Facebook and Twitter', 'Facebook and Twitter')], default='', max_length=20, null=True)),
                ('collaborators', models.ManyToManyField(blank=True, default=[], related_name='collaborators', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
