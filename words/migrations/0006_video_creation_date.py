# Generated by Django 3.0.6 on 2020-06-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='creation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
