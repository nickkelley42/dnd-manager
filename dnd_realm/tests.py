from django.test import TestCase
from .models import Realm, Character

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
