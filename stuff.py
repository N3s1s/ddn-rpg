import abc
from random import randrange
from inspect import *
from caracteristic import *

class Stuff(abc.ABC):
    def __init__(self, name, description):
        self.id = randrange(1, 1000)
        self.name = name
        self.description = description


class Weapon(Stuff):
    def __init__(self, carrier, name, description, damage, resistance, strength=0):
        super().__init__(name, description)
        self.damage = damage
        self.resistance = resistance

    # def __repr__(self):
    #     return self.name
    #
    # def __str__(self):
    #     return str(self.id)

class ArmorPiece(Stuff):
    def __init__(self, owner, name, description, location, normal_armor, magic_armor):
        super().__init__(name, description)
        self.location = location
        self.armor = Armor(normal_armor, magic_armor)
        # owner.armor.current += self.armor.current
        # self.add_caracterisic(owner)

    # def add_caracterisic(self, owner):
    #     print(owner.name)
    #     for var in vars(self):
    #         if var in ['armor']:
    #             print(var)
    #             print(getattr(getattr(owner, var), 'current'))
    #             setattr(getattr(getattr(owner, var), 'current', + getattr(self.var)))


        # print(getattr(carrier, 'name'))
        # for var in vars(self):
        #     if var in ['armor']:
        #         print(vars(self))
        #         print(getattr(carrier, var))
