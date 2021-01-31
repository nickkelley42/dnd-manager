from django.db import models

class Realm(models.Model):
    name = models.CharField(max_length=30)

class Character(models.Model):
    name = models.CharField(max_length=30, default="")

    realm = models.ForeignKey(Realm, on_delete=models.SET_NULL, null=True)

    base_strength = models.IntegerField(default=0)
    base_dexterity = models.IntegerField(default=0)
    base_constitution = models.IntegerField(default=0)
    base_intelligence = models.IntegerField(default=0)
    base_wisdom = models.IntegerField(default=0)
    base_charisma = models.IntegerField(default=0)
