# Generated by Django 3.1.5 on 2021-01-31 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0004_character_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='realm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dnd_realm.realm'),
        ),
    ]