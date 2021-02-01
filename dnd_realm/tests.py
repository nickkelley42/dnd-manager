from django.test import TestCase
from .models import Character, Realm, Trait

from math import floor

# Create your tests here.

class RealmModelTests(TestCase):
    def test_realm_model_exists(self):
        """
        the realm model should exist and be instantiatable.
        """
        realm = Realm()
        self.assertIsInstance(realm, Realm)

    def test_realm_model_has_name(self):
        """
        The realm model should have a name string attribute
        """
        realm = Realm()
        self.assertIsInstance(realm.name, str)

    def test_realm_has_many_characters(self):
        """
        A realm may have multiple associated characters
        """
        realm = Realm()
        realm.save()
        for i in range(3):
            realm.character_set.create()
        self.assertEqual(len(realm.character_set.all()), 3)


class CharacterModelTests(TestCase):
    def test_character_model_exists(self):
        """
        Character model should exist
        """
        character = Character()
        self.assertIsInstance(character, Character)

    def test_character_model_has_name(self):
        """
        Characters must have a name
        """
        character = Character()
        self.assertIsInstance(character.name, str)

    def test_character_has_base_abilities(self):
        """
        Character models have base ability scores.
        """
        character = Character()
        self.assertIsInstance(character.base_strength, int)
        self.assertIsInstance(character.base_dexterity, int)
        self.assertIsInstance(character.base_constitution, int)
        self.assertIsInstance(character.base_intelligence, int)
        self.assertIsInstance(character.base_wisdom, int)
        self.assertIsInstance(character.base_charisma, int)

    def test_character_strength_modifier(self):
        """
        Character ability modifiers are derived from base stats
        """
        c = Character()
        for i in range(1, 31):
            c.base_strength = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.strength_modifier, expected)
        for i in range(1, 31):
            c.base_dexterity = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.dexterity_modifier, expected)
        for i in range(1, 31):
            c.base_constitution = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.constitution_modifier, expected)
        for i in range(1, 31):
            c.base_intelligence = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.intelligence_modifier, expected)
        for i in range(1, 31):
            c.base_wisdom = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.wisdom_modifier, expected)
        for i in range(1, 31):
            c.base_charisma = i
            expected = floor((i - 10) / 2)
            self.assertEqual(c.charisma_modifier, expected)

    def test_character_has_traits(self):
        """
        traits provide bonuses for the character
        """
        c = Character()
        c.save()
        t = Trait(
            name='my trait',
            strength_bonus=1,
            dexterity_bonus=1,
            constitution_bonus=1,
            intelligence_bonus=1,
            wisdom_bonus=1,
            charisma_bonus=1
        )
        t.save()
        c.trait_set.add(t)

        self.assertEqual(c.strength, 1, "strength is base + bonus")
        self.assertEqual(c.dexterity, 1, "strength is base + bonus")
        self.assertEqual(c.constitution, 1, "strength is base + bonus")
        self.assertEqual(c.intelligence, 1, "strength is base + bonus")
        self.assertEqual(c.wisdom, 1, "strength is base + bonus")
        self.assertEqual(c.charisma, 1, "strength is base + bonus")

class UrlStructureTests(TestCase):
    def test_realm_index(self):
        """
        Verify that getting a realm by id works
        """
        realm = Realm(name="my realm")
        realm.save()

        response = self.client.get('/realm/%d' % realm.id)

        self.assertTrue(response.status_code == 200, "response has 200 status")
        self.assertTrue(realm.name.encode() in response.content, "response includes the name of the realm")
