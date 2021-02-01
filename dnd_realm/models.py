from django.db import models
from math import floor

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

    def _modifier_from_stat(self, stat):
        return floor((stat - 10) / 2)

    @property
    def strength_modifier(self):
        return self._modifier_from_stat(self.base_strength)
    @property
    def dexterity_modifier(self):
        return self._modifier_from_stat(self.base_dexterity)
    @property
    def constitution_modifier(self):
        return self._modifier_from_stat(self.base_constitution)
    @property
    def intelligence_modifier(self):
        return self._modifier_from_stat(self.base_intelligence)
    @property
    def wisdom_modifier(self):
        return self._modifier_from_stat(self.base_wisdom)
    @property
    def charisma_modifier(self):
        return self._modifier_from_stat(self.base_charisma)
