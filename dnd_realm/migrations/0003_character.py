# Generated by Django 3.1.5 on 2021-01-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_realm', '0002_realm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
