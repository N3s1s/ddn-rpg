import abc
from attribut import *


class CharacterClasse(abc.ABC):
    pass


class Warrior(CharacterClasse):
    name = "warrior"
    attribut = [Debile, Resistant]


class Ranger(CharacterClasse):
    pass
