import random

class StatusEffect:
    def __init__(self, name):
        self.name = name

class Burn(StatusEffect):
    class Burn(StatusEffect):
        def __init__(self):
            super().__init__("Burn")
            self.damage_percentage = 0.125  # In the original games, burn caused a fixed 1/8 of max HP damage each turn
            self.attack_reduction = 0.5  # In the original games, burn cuts the attack stat in half

        def apply_effect(self, pokemon):
            if pokemon.hp == pokemon.max_hp and pokemon.status != "Burn":
                damage = int(pokemon.max_hp * self.damage_percentage)
                pokemon.hp -= damage
                pokemon.status = "Burn"
                pokemon.attack *= self.attack_reduction
                print("{} was hurt by its burn! It took {} damage.".format(pokemon.name, damage))
            elif pokemon.hp > 0:
                damage = int(pokemon.max_hp * self.damage_percentage)
                pokemon.hp -= damage
                print("{} was hurt by its burn! It took {} damage.".format(pokemon.name, damage))
            if pokemon.hp <= 0:
                print("{} has fainted due to its burn.".format(pokemon.name))
                pokemon.fainted = True

        def remove_effect(self, pokemon):
            pokemon.status = None
            pokemon.attack /= self.attack_reduction
            print("{}'s burn has been healed.".format(pokemon.name))

class Freeze(StatusEffect):
    def __init__(self):
        super().__init__("Freeze")
    def apply_effect(self, pokemon):
        if pokemon.hp == pokemon.max_hp and pokemon.status != "Frozen":
            pokemon.status = "Frozen"
            if random.randint(0,100) < 20:
                print("{} is thawed out!".format(pokemon.name))
                pokemon.status = None
            else:
                print("{} is frozen solid!".format(pokemon.name))
        elif pokemon.status == "Frozen":
            print("{} is already frozen!".format(pokemon.name))
        else:
            print("{} can't be frozen!".format(pokemon.name))

class Paralysis(StatusEffect):
    def __init__(self):
        super().__init__("Paralysis")
    def apply_effect(self, pokemon):
        if pokemon.hp == pokemon.max_hp and pokemon.status != "Paralyzed":
            if random.randint(0,100) < 25:
                print("{} is fully paralyzed! It can't move!".format(pokemon.name))
                pokemon.status = "Paralyzed"
            else:
                print("{} is paralyzed! Its speed is halved.".format(pokemon.name))
                pokemon.status = "Paralyzed"
        elif pokemon.status == "Paralyzed":
            print("{} is already paralyzed!".format(pokemon.name))
        else:
            print("{} can't be paralyzed!".format(pokemon.name))

class Poison(StatusEffect):
    def __init__(self):
        super().__init__("Poison")
    def apply_effect(self, pokemon):
        if pokemon.hp == pokemon.max_hp and pokemon.status != "Poisoned":
            damage = int(pokemon.max_hp / 8)
            pokemon.hp -= damage
            pokemon.status = "Poisoned"
            print("{} is hurt by poison! It took {} damage.".format(pokemon.name, damage))
            if pokemon.hp <= 0:
                print("{} has fainted.".format(pokemon.name))
        elif pokemon.status == "Poisoned":
            damage = int(pokemon.max_hp / 8)
            pokemon.hp -= damage
            print("{} is hurt by poison! It took {} damage.".class Sleep(StatusEffect):

    class Sleep(StatusEffect):
        def __init__(self, turns=None):
            super().__init__("Sleep")
            if turns is None:
                self.turns = random.randint(1, 3)
            else:
                self.turns = turns

        def apply_effect(self, pokemon):
            if self.turns > 0:
                print("{} is fast asleep.".format(pokemon.name))
                self.turns -= 1
            else:
                print("{} woke up!".format(pokemon.name))
                pokemon.status = None

    class Toxic(StatusEffect):
        def __init__(self):
            super().__init__("Toxic")
            self.damage_percentage = 0.125

        def apply_effect(self, pokemon):
            damage = int(pokemon.max_hp * self.damage_percentage)
            pokemon.hp -= damage
            print("{} is hurt by toxic! It took {} damage.".format(pokemon.name, damage))
            if pokemon.hp <= 0:
                print("{} fainted.".format(pokemon.name))
                pokemon.fainted = True

    class Confusion(StatusEffect):
        def __init__(self):
            super().__init__("Confusion")
            self.turns = random.randint(1, 3)

        def apply_effect(self, pokemon):
            if self.turns > 0:
                self.turns -= 1
                if random.randint(0, 100) < 25:
                    print("{} is confused and hurt itself.".format(pokemon.name))
                    damage = int(pokemon.max_hp * 0.125)
                    pokemon.hp -= damage
                    if pokemon.hp <= 0:
                        print("{} fainted.".format(pokemon.name))
                        pokemon.fainted = True
                else:
                    print("{} is confused.".format(pokemon.name))
            else:
                print("{} snapped out of confusion!".format(pokemon.name))
                pokemon.status = None
