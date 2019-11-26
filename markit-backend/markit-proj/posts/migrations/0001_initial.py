# Generated by Django 2.2.6 on 2019-11-25 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=9)),
                ('image', models.ImageField(default='posts/postDefault.png', upload_to='posts/')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='calendars.Calendar')),
            ],
        ),
    ]
