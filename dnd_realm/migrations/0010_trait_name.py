# Generated by Django 3.1.5 on 2021-02-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0009_auto_20210201_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
