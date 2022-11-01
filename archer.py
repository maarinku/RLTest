class Archer():
    def __init__(self, type, level):
        self.level = level
        self.type = archer
        self.maxhealth = 100
        self.health = 100
        self.attack = 20
        self.money = 0
        self.crit = 0.3
        self.items = []
        print(f"Spawned Archer")