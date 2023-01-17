class Stats:
    def __init__(self):
        self.defense = 0
        self.speed = 0
        self.sp_defense = 0
        self.attack = 0
        self.defense_stage = 0
        self.speed_stage = 0
        self.sp_defense_stage = 0
        self.attack_stage = 0

    def lower_defense(self):
        self.defense = max(0, self.defense - 1)
        self.defense_stage -= 1

    def raise_defense(self):
        self.defense += 2
        self.defense_stage += 1

    def lower_speed(self):
        self.speed = max(0, self.speed - 1)
        self.speed_stage -= 1

    def raise_speed(self):
        self.speed += 2
        self.speed_stage += 1

    def lower_sp_defense(self):
        self.sp_defense = max(0, self.sp_defense - 1)
        self.sp_defense_stage -= 1

    def raise_sp_defense(self):
        self.sp_defense += 2
        self.sp_defense_stage += 1

    def lower_sp_attack(self):
        self.sp_attack = max(0, self.sp_attack - 1)
        self.sp_attack_stage -= 1

    def raise_sp_attack(self):
        self.sp_attack += 2
        self.sp_attack_stage += 1
