from enemy import *
from archer import *
from types import *

def attack(point):
    damage = enemy.attack
    point = point - damage
    print(f"{enemy.enemytype} damage is {enemy.attack}")
    return point

def attack_enemy(Enemy):
    damage = 