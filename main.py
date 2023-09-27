from character import Player
from race import Human
from character_class import Warrior
from stuff import Weapon
from stuff import ArmorPiece
from random import randrange


Nesis = Player(name="Nesis", race=Human, character_class=Warrior, life=50, mana=25, courage=10, intelligence=11, charisma=9, dexterity=12, strength=11, attack=9, parade=12, level=2)
# Malbrook = Player(name="Malbrook", race=Human, character_class=Warrior, life=40, mana=0, courage=12, intelligence=8, charisma=13, dexterity=10, strength=11, attack=9, parade=12, level=3)

Nesis.stuff.append(ArmorPiece(Nesis, "plastron", "un simple plastron", 'torso', 4, 2))



for item in Nesis.stuff:
    print(item.name + ' ' + str(item.armor.total))
    item.armor.normal += 2
    print(item.name + ' ' + str(item.armor.total))

# print(Nesis.armor.base)
# print(Nesis.armor.current)
# Nesis.stuff.append(ArmorPiece(Nesis, "plastron", "un simple plastron", 'torso', 4, 2))
# Nesis.stuff.append(ArmorPiece(Nesis, "jambière", "une simple jambière", 'leg', 3, 1))
# print(Nesis.armor.base)
# print(Nesis.armor.current)
# print(Nesis.armor.normal)
# print(Nesis.armor.magic)

# Nesis.stuff.append(Weapon(Nesis, name="épée", description="une simple épée", damage=12, resistance=6, strength=6))
# Nesis.stuff.append(Weapon(Nesis, name="épée", description="une simple épée", damage=12, resistance=6, strength=6))
# print(*Nesis.stuff)
# print(' '.join(map(str, Nesis.stuff)))

# Nesis.stuff("add", Weapon(name="épée", description="une simple épée", damage=12, resistance=6, strength=6))
# Nesis.stuff("listing")
# Nesis.stuff("remove")
# , object=(Weapon(name="épée", description="une simple épée", damage=12, resistance=6, strength=6)))



# print(Nesis.life.start)
# print(Nesis.life.max)
# print(Nesis.life.current)
#
# print(Nesis.life.current)
# Nesis.life.modify('current', -3)
# print(Nesis.life.current)

# print(Malbrook.life.start)
# print(Malbrook.life.max)
# print(Malbrook.life.current)
#
# Malbrook.life.modify_current(-3)
#
# print(Malbrook.life.current)

# print(Nesis.name
#       + ' is an '
#       + Nesis.race.name
#       + " of class "
#       + Nesis.character_class.name
#       + ' with '
#       + str(Nesis.current_life)
#       + ' life point, '
#       + str(Nesis.current_mana)
#       + ' points of mana and '
#       + str(Nesis.destiny)
#       + ' destiny points')

# print(Nesis.magic_resistance_test())
# Nesis.intelligence = 20
# print(Nesis.magic_resistance_test())

# for attribut in Nesis.attribut:
#     print(attribut)

# for ability in Nesis.ability:
#     print(ability)

# for capacity in Nesis.capacity:
#     print(capacity)

# for item in Nesis.stuff:
#     print(item.name)

# print(Nesis.calculate_normal_armor())
# print(Nesis.calculate_total_armor())
# print(Nesis.total_armor)
# print(Nesis.normal_armor_test(8))

# Nesis.stuff.append(Weapon(name="épée", description="une simple épée", damage=12, resistance=6, strength=6))
# print(Nesis.stuff[0].strenght)
# Nesis.stuff.append(Weapon("arc", "un arc", 20, 2))
# print(Nesis.stuff[1].strenght)
# Nesis.stuff.append(ArmorPiece("casque", "une simple casque", 'head', 2, 0))

# print(Nesis.armor.current)
# Nesis.stuff.append(ArmorPiece(Nesis.name, "plastron", "un simple plastron", 'torso', 4, 2))
# Nesis.stuff.append(ArmorPiece("jambière", "une simple jambière", 'leg', 3, 1))

# for item in Nesis.stuff:
#     print(item.name
#           + ' current: ' + str(item.armor.current)
#           + ' start: ' + str(item.armor.start)
#           + ' max: ' + str(item.armor.max)
#           + ' normal: ' + str(item.armor.normal)
#           + ' magic: ' + str(item.armor.magic)
#           + ' total: ' + str(item.armor.total))

# print(Nesis.armor.total)
# print(Nesis.calculate_armor2())
# print(Nesis.armor.normal)
# print(Nesis.armor.magic)

# print(Nesis.calculate_normal_armor())

# print(Nesis.calculate_armor("normal_armor"))

# print(Nesis.dexterity)

# print(Nesis.caracteristics_test(randrange(1, 20), "dexterity"))

# print(Nesis.caracteristics_test(randrange(1, 20), "magic_resistance"))

# print(Nesis.calculate_armor("normal_armor"))
# print(Nesis.calculate_armor("magic_armor"))
# print(Nesis.calculate_armor("total_armor"))
# print(Nesis.calculate_armor())

