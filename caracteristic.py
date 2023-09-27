from character import *

class Caracteristic:
    def __init__(self, start):
        self.base = start
        self.max = start
        self.current = start
    
    def modify(self, attribute, modifier):
        return setattr(self, attribute, getattr(self, attribute) + modifier)


class Life(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Mana(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Level(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Courage(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Intelligence(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Charisma(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Dexterity(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Strenght(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Attack(Caracteristic):
    def __init__(self, start):
        super().__init__(start)


class Parade(Caracteristic):
    def __init__(self, start):
        super().__init__(start)

class Armor(Caracteristic):
    def __init__(self, normal, magic):
        self.normal = normal
        self.magic = magic
        # self.total = normal + magic
        super().__init__(self.total)

    @property
    def total(self):
        return self.normal + self.magic

