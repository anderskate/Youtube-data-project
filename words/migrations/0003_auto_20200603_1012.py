# Generated by Django 3.0.6 on 2020-06-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_key_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='word',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]