from caracteristic import *

class Attribut:
    pass


class Resistant(Attribut):
    name = "Résistant"
    armor = Armor(1, 0)


class Debile(Attribut):
    name = "Débile"
    armor = Armor(0, -1)


class Polyvalent(Attribut):
    name = "Polyvalent"


class Faible(Attribut):
    name = "Faible"
