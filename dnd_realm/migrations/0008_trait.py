# Generated by Django 3.1.5 on 2021-02-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0007_auto_20210131_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.ManyToManyField(to='dnd_realm.Character')),
            ],
        ),
    ]
