# Generated by Django 3.1.5 on 2021-01-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0003_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
