# Generated by Django 3.1.5 on 2021-01-31 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
