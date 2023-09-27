import abc
from attribut import *


class Race(abc.ABC):
    pass


class Human(Race):
    name = "human"
    attribut = [Polyvalent, Faible]
    ability = ["érudit", "forgeron"]
    capacity = ["coup de poing", "mensonge"]


class Dwarf(Race):
    pass
