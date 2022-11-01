from enemy import *
from archer import *
from types import *

print("Choose your player class:")
print("     [1] Archer")
choice = int(input("Class: "))

if choice == 1:
    return Archer