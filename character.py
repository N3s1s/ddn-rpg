import abc
import math
from caracteristic import *

class BaseCharacter:
    """Abstract base class for all characters."""

    def __init__(self, name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, armor, level):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.life = life
        self.level = level
        self.mana = mana
        self.courage = courage
        self.intelligence = intelligence
        self.charisma = charisma
        self.dexterity = dexterity
        self.strength = strength
        self.attack = attack
        self.parade = parade
        self.armor = armor
        self.stuff = []
        self.weapon = []
        self.inventory = []
        self.attribut = self.character_class.attribut + self.race.attribut
        self.ability = self.race.ability
        self.capacity = self.race.capacity
        self.magic_resistance = self.calculate_magic_resistance()

    def calculate_magic_resistance(self):
        """Calculate and return the magic resistance value."""
        return (self.courage.current + self.intelligence.current + self.strength.current) // 3

class Npc(BaseCharacter):
    """Class representing non-player characters."""
    pass

class Player(BaseCharacter):
    """Class representing player characters."""

    def __init__(self, name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, destiny=0, experience=0, level=1):
        super().__init__(name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, level)
        self.experience = Caracteristic(experience)
        self.destiny = Caracteristic(destiny)