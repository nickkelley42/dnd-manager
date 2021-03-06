# Generated by Django 3.1.5 on 2021-01-31 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0005_character_realm'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='base_charisma',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='base_constitution',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='base_dexterity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='base_intelligence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='base_strength',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='base_wisdom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
