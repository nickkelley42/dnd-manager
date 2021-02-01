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

    @property
    def strength(self):
        strength = self.base_strength
        for t in self.trait_set.all():
            strength += t.strength_bonus
        return strength

    @property
    def dexterity(self):
        dexterity = self.base_dexterity
        for t in self.trait_set.all():
            dexterity += t.dexterity_bonus
        return dexterity

    @property
    def constitution(self):
        constitution = self.base_constitution
        for t in self.trait_set.all():
            constitution += t.constitution_bonus
        return constitution

    @property
    def intelligence(self):
        intelligence = self.base_intelligence
        for t in self.trait_set.all():
            intelligence += t.intelligence_bonus
        return intelligence

    @property
    def wisdom(self):
        wisdom = self.base_wisdom
        for t in self.trait_set.all():
            wisdom += t.wisdom_bonus
        return wisdom

    @property
    def charisma(self):
        charisma = self.base_charisma
        for t in self.trait_set.all():
            charisma += t.charisma_bonus
        return charisma

class Trait(models.Model):
    characters = models.ManyToManyField(Character)

    name = models.CharField(max_length=30, default="")

    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    constitution_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    wisdom_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)

