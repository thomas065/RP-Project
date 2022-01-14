from dataclasses import dataclass
from pygame import mixer
import random
import time
import sys
import random
import time
from termcolor import colored, cprint
from colorama import init
init()

# Choosing an Avatar
@dataclass
class Human:
    strength: float = 4
    stamina:float = 60
    atk: float = 4
    exp: float = 0
    level: float = 1

@dataclass
class Elf(Human):
    strength: float = 2
    stamina: float = 25
    atk: float = 2

@dataclass
class Orc(Human):
    strength: float = 10
    stamina: float = 80
    atk: float = 10

@dataclass
class Dwarf(Human):
    strength: float = 6
    stamina: float = 100
    atk: float = 10

# Choosing your sub-class
@dataclass
class Wizard():
    magika: float = 100
    mag_atk: float = 8

@dataclass
class Warrior():
    berserk: float = 100

@dataclass
class Thief():
    courage: float = 100

@dataclass
class Priest():
    magika: float = 100
    mag_atk: float = 6

def avatar_select():
    print("")
    print("------------------------------------------")
    print("|       === Select your Avatar ===       |")
    print("------------------------------------------")
    print("| 1.  Human        | 2.   Elf            |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.  Orc          | 4.    Dwarf         |")
    print("------------------------------------------")
    print("| 5. Quit Game                           |")
    print("------------------------------------------")
    while True:
        option = input("Choose your Avatar: ")
        print()
        if option == "1":
            print("You have chosen:\n",Human())
            break
        if option == "2":
            print("You have chosen:\n", Elf())
            break
        if option == "3":
            print("You have chosen:\n", Orc())
            break
        if option == "4":
            print("You have chosen:\n", Dwarf())
            break
        elif option == "5":
            print("Goodbye!")
            exit()

def class_select():
    print("------------------------------------------")
    print("|     === Select your Sub-class ===      |")
    print("------------------------------------------")
    print("| 1.  Wizard        | 2.   Warrior       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.  Thief         | 4.    Priest       |")
    print("------------------------------------------")
    print("| 5. <-- Return                          |")
    print("------------------------------------------")
    while True:
        option = input("Choose your Sub-class: ")
        print()
        if option == "1":
            print("You have added attributes:\n",Wizard())
            break
        if option == "2":
            print("You have added attributes:\n", Warrior())
            break
        if option == "3":
            print("You have added attributes:\n", Thief())
            break
        if option == "4":
            print("You have added attributes:\n", Priest())
            break
        elif option == "5":
            break

def Loading():
    bed = (0.01, 0.03, 0.05)
    pillow = random.choice(bed)
    def progress(percent=0, width=20):
        hashes = width * percent // 100
        blanks = width - hashes
        print('\rLoading....[', hashes * '#', blanks * ' ', ']', f' {percent:.0f}%', sep='',
            end='', flush=True)
    for i in range(101):
        progress(i)
        time.sleep(pillow)
    print()

print()
traveler = input("Enter your name, Traveler:\n")
Loading()
print(f"""
Welcome {traveler}, to Hang-Out Dungeon!\n
Here, you will choose between 4 Avatar's with varying types of attributes and
4 sub-classes of varying types of attributes.
You will loot treasure, gain levels and experience, fight random monsters and come
in contact with strangers of misfortune.\n(*** Please BEWARE, everything in this game is a W-I-P ***)
""")
time.sleep(2.5)

avatar_select()
class_select()

while True:
    check = input("Do you wish to change your Avatar? Y/N ")
    if check.casefold() == "y":
        avatar_select()
        class_select()
    if check.casefold() == "n":
        break

print(f"Okay {traveler}, you have selected your arsenal")
time.sleep(1.5)
print()
print("Let's play a quick game to get you warmed up")
Loading()
print()

high_score = 0
def dice_game():
    global high_score
    print(f"Current High Score: {high_score} ")
    print("1) Roll Dice")
    print("2) Leave Game")
    user_input = input("Enter your choice: ")
    print()
    while user_input == "1":
            battle_dice_one = random.randint(1, 6)
            battle_dice_two = random.randint(1, 6)
            total = battle_dice_one + battle_dice_two
            print(f"You roll a... {battle_dice_one}")
            print(f"You roll a... {battle_dice_two}")
            print()
            print(f"You have rolled a total of {total}")
            print()
            if total > high_score:
                print("New High Score!")
                print()
                high_score = total
            else:
                pass
            dice_game()
    if user_input == "2":
        print("Goodbye!")
        exit()
dice_game()
