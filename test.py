from random import randrange, choice


class Npc:
    def __init__(self, name, armor, life, dodge, state):
        self.name = name
        self.armor = armor
        self.life = life
        self.state = state
        self.dodge = dodge

    def subtract_armor(self, spell):
        return spell - self.armor

    def reduce_life(self, damage):
        self.life = self.life - damage
        if self.life <= 0:
            self.dead()
            return "dead"

    def dead(self):
        print(self.name + " is dead !")
        self.state.remove("alive")
        self.state.append("dead")

    def try_dodge(self):
        if randrange(1, 20) < self.dodge:
            return True
        else:
            return False

    def critic_fail_attack(self):
        roll = randrange(1, 21)
        match roll:
            case 1 | 2:
                print('Rattrape son erreur in extremis')
            case 3 | 4 | 5:
                print('Trébuche et chute maladroitement')
            case 6 | 7:
                print("Frappe l'allié de gauche")
            case 8 | 9:
                print("Frappe l'allié de droite")
            case 10 | 11 | 12:
                print('Lâche son arme comme un looser')
            case 13 | 14 | 15:
                print('Casse son arme')
            case 16 | 17 | 18:
                print('Se blesse tout seul comme un cake')
            case 19:
                print('Se blesse très sévèrement de façon atroce et douloureuse')
            case 20:
                print('Perd un oeil')


class Orc(Npc):
    pass


class Player(Npc):
    def __init__(self, name, life, armor, hit, weapon):
        self.name = name
        self.life = life
        self.armor = armor
        self.weapon = weapon
        self.hit = hit

    def attack(self, aim, weapon):
        print(self.name + " attack " + aim.name + ' with ' + weapon.name)
        print(aim.name + ' have ' + str(aim.life) + " life and " + str(aim.armor) + " armor")
        damage = aim.subtract_armor(weapon.damage)
        match(weapon.test_hit(self.hit)):
            case "critic_success":
                aim.reduce_life((weapon.damage * 3))
                print('Critic !' + " Make " + str(weapon.damage * 3) + " damage points")
            case "critic_fail":
                print('Critic fail ! ')
                self.critic_fail_attack()
            case True:
                if aim.try_dodge():
                    print(aim.name + " dodge attack !")
                else:
                    print(aim.name + " take " + str(damage) + " of damage, still " + str(aim.life) + " points of life")
            case False:
                print('Attack missing')

    def list_weapon(self):
        for x in self.weapon:
            print(self.name + " have " + x.name + " deal " + str(x.damage) + " points")


class Weapon:
    def __init__(self, name, weapon_type, damage):
        self.name = name
        self.type = weapon_type
        self.damage = damage

    def test_hit(self, player_attack):
        roll = randrange(1, 21)
        print(roll)
        if roll == 1:
            return "critic_success"
        elif roll == 20:
            return "critic_fail"
        elif roll > player_attack:
            return True
        else:
            return False

sword1 = Weapon("Epee Vorpal", "sword", 8)
bow1 = Weapon("Arc de Lunelbar", "bow", 16)
player1 = Player("Nesis", 20, 12, 12, [sword1, bow1])
orc1 = Orc("Reivaxx", 6, 10, 8, ["alive", "hurt"])

player1.list_weapon()
player1.attack(orc1, choice(player1.weapon))
