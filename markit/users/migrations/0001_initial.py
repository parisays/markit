# Generated by Django 2.2.6 on 2019-10-21 16:41

from django.db import migrations, models
import stdimage.models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('firstName', models.CharField(max_length=50, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('profileImage', stdimage.models.StdImageField(blank=True, default='/static/profile.jpg', upload_to='profileImage', verbose_name='Profile Picture')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
