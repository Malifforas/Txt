class Pokemon:
    def __init__(self, name, move_list, stats):
        self.name = name
        self.move_list = move_list
        self.stats = stats
        self.hp = stats["hp"]
        self.level = 1
        self.is_caught = False
        self.catch_rate = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("{} fainted.".format(self.name))

    def use_move(self, move):
        pass

