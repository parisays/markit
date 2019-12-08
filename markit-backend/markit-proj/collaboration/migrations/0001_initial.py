# Generated by Django 2.2.6 on 2019-12-08 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', jsonfield.fields.JSONField()),
                ('role', models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Manager', 'Manager'), ('Editor', 'Editor'), ('Viewer', 'Viewer')], default='', max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
