import os
import random


class Player:
    def __init__(self, name, life, courage, attack, parade, alive=True, turn=0):
        self.name = name
        self.alive = alive
        self.life = Caracteristic(life)
        self.base_courage = Caracteristic(courage)
        self.base_normal_armor = Caracteristic(0)
        self.base_magic_armor = Caracteristic(0)
        self.base_attack = Caracteristic(attack)
        self.parade = Caracteristic(parade)
        self.turn = turn
        self.stuff = []
        self.damage = random.randrange(1, 8)

    def __str__(self):
        return str(self.name)

    @property
    def base_total_armor(self):
        base_total_armor = Caracteristic(
            self.base_normal_armor.current + self.base_magic_armor.current
        )
        return base_total_armor

    def caractereristic(self, value):
        if hasattr(self, f"base_{value}"):
            total = Caracteristic(getattr(self, f"base_{value}").current)
        else:
            total = 0
        for item in self.stuff:
            if hasattr(item, value):
                total.current += getattr(item, value).current
        return total

    def offensive(self, defender):
        print(self.name + " attack " + defender.name)
        weapon_list = []
        for item in self.stuff:
            if type(item).__name__ == "Weapon":
                weapon_list.append(item)
        weapon = None
        if len(weapon_list) != 0:
            print("Weapon:", *weapon_list, sep="\n")
            while weapon not in weapon_list:
                selected = input("=> ")
                weapon = next(
                    (weapon for weapon in weapon_list if weapon.name == selected), None
                )
        else:
            weapon = self
        if self.caractereristic("attack").roll:
            if not defender.parade.roll:
                print(f"damage : {weapon.damage}")
                print(
                    "ennemies armor :", defender.caractereristic("total_armor").current
                )
                real_damage = (
                    weapon.damage - defender.caractereristic("total_armor").current
                )
                if real_damage >= 1:
                    defender.life.current -= real_damage
                    print(self.name, "make", real_damage, "of damage")
                    if defender.life.current <= 0:
                        print(defender.name + " is dead !")
                        defender.alive = False
                else:
                    print(
                        self.name,
                        f"succeeded attack but {defender.name} armor take the hit",
                    )
            else:
                print(defender.name, "parry attack")
        else:
            print(self.name, "failed is attack")


class Caracteristic:
    def __init__(self, start):
        self.base = start
        self.max = start
        self.current = start

    @property
    def roll(self):
        dice_roll = random.randrange(1, 20)
        if dice_roll <= self.current:
            return True
        else:
            return False


class Stuff:
    def __init__(self, name, description):
        self.id = random.randrange(1, 1000)
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.name)


class Weapon(Stuff):
    def __init__(self, name, description, location, damage, resistance, attack):
        super().__init__(name, description)
        self.location = location
        self.damage = damage
        self.attack = Caracteristic(attack)
        self.resistance = resistance


class ArmorPiece(Stuff):
    def __init__(
        self, name, description, location, normal_armor, magic_armor, courage=0
    ):
        super().__init__(name, description)
        self.location = location
        self.normal_armor = Caracteristic(normal_armor)
        self.magic_armor = Caracteristic(magic_armor)
        self.courage = Caracteristic(courage)

    @property
    def total_armor(self):
        total_armor = Caracteristic(
            self.normal_armor.current + self.magic_armor.current
        )
        return total_armor


class Fight:
    def __init__(self):
        self.players_team = []
        self.ennemies_team = []

    @property
    def fighters(self):
        listing = []
        for player in self.players:
            listing.append(player)
        for ennemie in self.ennemies:
            listing.append(ennemie)
        return listing

    @property
    def players(self):
        listing = []
        for player in self.players_team:
            if player.alive:
                listing.append(player)
        return listing

    @property
    def ennemies(self):
        listing = []
        for ennemie in self.ennemies_team:
            if ennemie.alive:
                listing.append(ennemie)
        return listing

    @property
    def ordered(self):
        listing = []
        for fighter in sorted(
            (self.players + self.ennemies),
            key=lambda x: x.caractereristic("courage").current,
            reverse=True,
        ):
            listing.append(fighter)
        return listing

    def add_fighter(self, name, team):
        if team == "player_team":
            self.players_team.append(
                Player(
                    name,
                    random.randrange(12, 18),
                    random.randrange(9, 13),
                    random.randrange(10, 14),
                    random.randrange(10, 14),
                )
            )
        elif team == "ennemies_team":
            self.ennemies_team.append(
                Player(
                    name,
                    random.randrange(6, 13),
                    random.randrange(6, 10),
                    random.randrange(5, 10),
                    random.randrange(5, 10),
                )
            )

    def start(self):
        for attacker in self.ordered:
            attacker.turn = 0
        while any(player.alive for player in self.players) and any(
            ennemie.alive for ennemie in self.ennemies
        ):
            for attacker in self.ordered:
                if attacker.alive:
                    if attacker in self.players:
                        target_list = self.ennemies
                    else:
                        target_list = self.players
                    if any(defender.alive for defender in target_list):
                        attacker.turn += 1
                        print(attacker.name, "turn", attacker.turn)
                        print("Target:", *target_list, sep="\n")
                        defender = None
                        while defender not in target_list:
                            selected = input("=> ")
                            defender = next(
                                (
                                    target
                                    for target in target_list
                                    if target.name == selected
                                ),
                                None,
                            )
                        os.system("clear")
                        attacker.offensive(defender)
                        input("Continue ?")
                        os.system("clear")
        print("victory for", *self.fighters)


player_list = ["Nesis", "Kubor", "Malbrook", "Doremie"]
npc_list = ["Reivaxx", "Zangdar", "gobelin"]

fight = Fight()

for npc_name in npc_list:
    fight.add_fighter(npc_name, "ennemies_team")

for player_name in player_list:
    fight.add_fighter(player_name, "player_team")

for fighters in fight.players_team + fight.ennemies_team:
    if fighters.name == "Nesis":
        fighters.stuff.append(
            ArmorPiece("plastron", "un simple plastron", "torso", 4, 2, 3)
        )
        fighters.stuff.append(ArmorPiece("casque", "un simple casque", "head", 2, 0))
        fighters.stuff.append(Weapon("épée", "une simple épée", "une main", 2, 0, 2))
        fighters.stuff.append(
            Weapon("épée deux mains", "une grande épée", "deux main", 4, 1, 3)
        )
    if fighters.name == "Malbrook":
        fighters.stuff.append(
            ArmorPiece("jambière", "une simple jambière", "leg", 3, 1)
        )
    if fighters.name == "Kubor":
        fighters.stuff.append(
            ArmorPiece("gants", "paire de gants épique", "leg", 3, 1, 20)
        )
        fighters.stuff.append(
            Weapon("dague", "une simple dague", "une main", 10, 0, -1)
        )
    if fighters.name == "Doremie":
        fighters.stuff.append(
            Weapon("dague", "une simple dague", "une main", 10, 0, -1)
        )
    if fighters.name == "Reivaxx":
        fighters.stuff.append(ArmorPiece("casque", "un simple casque", "head", 2, 0))

# for player in fight.players_team:
#     values_list = ("attack", )
#     for value in values_list:
#         print(player.name, "have", player.caractereristic(value).current, value, "( base :", getattr(player, f"base_{value}").current, ")")
#         for item in player.stuff:
#             if hasattr(item, value):
#                 print(item.name, "with", getattr(item, value).current)
#         print(f"roll {value} :", player.caractereristic(value).roll)

fight.start()
