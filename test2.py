import os
import random
from operator import attrgetter


class Player:
    def __init__(self, name, courage, life, age=0, fight_round=0, alive=True):
        self.name = name
        self.alive = alive
        self.age = age
        self.life = Life(life)
        self.courage = courage
        self.fight_round = fight_round

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def attack(self):
        return self.name + " attack"


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


class Fight:
    def __init__(self, players, ennemies, turn=0):
        self.turn = turn
        self.players_team = players
        self.ennemies_team = ennemies

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
        for fighter in sorted((self.players + self.ennemies), key=attrgetter('courage'), reverse=True):
            listing.append(fighter)
        return listing


entry = ["Nesis", "Kubor", "Malbrook", "Dorémie"]
players_list = []
entry2 = ["Reivaxx", "Zangdar", "gobelin"]
ennemies_list = []

for x in entry:
    players_list.append(Player(x, random.randrange(1, 20), random.randrange(1, 20)))

for x in entry2:
    ennemies_list.append(Player(x, random.randrange(1, 20), random.randrange(1, 20)))


def attack(assailant, defender):
    ran2 = random.randrange(0, 8)
    print(assailant.name + " attack " + defender.name + " with " + str(ran2) + " damage")
    defender.life.current += -ran2
    if defender.life.current <= 0:
        print(defender.name + " is dead !")
        defender.alive = False


fight = Fight(players_list, ennemies_list)


while any(x.alive for x in fight.players) and any(x.alive for x in fight.ennemies):
    for attacker in fight.ordered:
        if attacker.alive:
            if attacker in fight.players_team:
                target = fight.ennemies
            else:
                target = fight.players
            if any(defender.alive for defender in target):
                print(f"{attacker.name}'s target:", *target, sep='\n')
                defender = None
                while defender not in target:
                    selected = input("=> ")
                    defender = next((obj for obj in target if obj.name == selected), None)
                os.system('clear')
                attack(attacker, defender)
                continuation = input("Continue ?")
                os.system('clear')
print('victory for', fight.fighters)

# def init_fight(player, ennemies):
#     fights = Fight(player, ennemies)
#     ran = random.randrange(0, 2)
#     for x in fights.ordered:
#         if x in player:
#             target = ennemies
#         elif x in ennemies:
#             target = player
#         print(f"{x.name}'s target:", *target, sep='\n')
#         select = input("=> ")
#         current = next((obj for obj in target if obj.name == select), None)
#         if attack(x, current) == "dead":
#             print(current.name + " is dead !")
#             if current in target:
#                 target.remove(current)
#             elif current in player(current):
#                 player.remove(current)

# def select_player():
#     print('Choice a player:', *player, sep='\n')
#     select = input("=> ")
#     current = next((obj for obj in player if obj.__str__() == select), None)
#     if current:
#         print("Select " + current.__str__() + " player, his age is " + str(current.age))
#         player_attack(current)
#         current.fight_round += 1
#     else:
#         select_player()
#     return current

# init_fight(player, ennemies)

# for x in player:
#     print(x.name + " " + str(x.life.current))
#     x.life.current += random.randrange(-5, 5)
#     print(x.name + " " + str(x.life.current))

# for x in fight.fighters:
#     print(x.name + " " + str(x.courage))

# print(max(fighters.courage for fighters in fight.fighters))

# def player_attack(fighter):
#     print("Player " + fighter.__str__() + " attack")

# choice = select_player()
# print(choice)


# for x in player:
#     print(x.fight_round)

# select_player()

# for x in player:
#     print(x.fight_round)
