# Generated by Django 2.2.6 on 2019-11-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20191107_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='postDefault.png', upload_to='posts/'),
        ),
    ]
