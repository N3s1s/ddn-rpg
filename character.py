import abc
import math
from caracteristic import *

class Character(abc.ABC):
    def __init__(self, name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, level):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.life = Life(life)
        self.level = Level(level)
        self.mana = Mana(mana)
        self.courage = Courage(courage)
        self.intelligence = Intelligence(intelligence)
        self.charisma = Charisma(charisma)
        self.dexterity = Dexterity(dexterity)
        self.strength = Strenght(strength)
        self.attack = Attack(attack)
        self.parade = Parade(parade)
        self.armor = Armor(0, 0)
        self.stuff = []
        self.weapon = []
        self.inventory = []
        self.attribut = self.character_class.attribut + self.race.attribut
        self.ability = self.race.ability
        self.capacity = self.race.capacity
        self.magic_resistance = math.floor((self.courage.current + self.intelligence.current + self.strength.current) / 3)

    def caracteristics_test(self, roll, caracteristics):
        if caracteristics == "magic_resistance":
            self.calculate_magic_resistance()
        if getattr(self, caracteristics) >= roll:
            return True
        else:
            return False

    # def stuff(self, action, object=""):
    #     match action:
    #         case "listing":
    #             for item in self.stuff_list:
    #                 print(item.name + ' ' + str(item.damage))
    #         case "add":
    #             self.stuff_list.append(object)
    #         case "remove":
    #             self.stuff_list.remove(object)

    def calculate_magic_resistance(self):
        self.magic_resistance = math.floor((self.courage + self.intelligence + self.strength) / 3)

    def calculate_armor(self, armor_type='total_armor'):
        self.normal_armor = 0
        self.magic_armor = 0
        self.total_armor = 0
        modifier_list = ['stuff', 'attribut']
        for modifier in modifier_list:
            for object in getattr(self, modifier):
                if hasattr(object, 'normal_armor'):
                    self.normal_armor += object.normal_armor
                if hasattr(object, 'magic_armor'):
                    self.magic_armor += object.magic_armor
        self.total_armor = self.normal_armor + self.magic_armor
        return getattr(self, armor_type)

    def calculate_armor2(self, armor_type='total'):
        modifier_list = ['stuff', 'attribut']
        for modifier in modifier_list:
            for object in getattr(self, modifier):
                if hasattr(object, 'armor'):
                    if hasattr(object.armor, 'normal'):
                        self.armor.normal += object.armor.normal
                    if hasattr(object.armor, 'magic'):
                        self.armor.magic += object.armor.magic
        self.armor.total = self.armor.normal + self.armor.magic
        return getattr(self.armor, armor_type)

    def calculate_strenght(self):
        modifier_list = ['stuff', 'attribut']
        for modifier in modifier_list:
            for object in getattr(self, modifier):
                if hasattr(object, 'strenght'):
                    self.strength += object.strenght

class Npc(Character):
    pass


class Player(Character):
    def __init__(self, name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, destiny=0, experience=0, level=1):
        super().__init__(name, race, character_class, life, mana, courage, intelligence, charisma, dexterity, strength, attack, parade, level)
        self.destiny = experience
        self.destiny = destiny
