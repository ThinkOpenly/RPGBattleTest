#!/usr/bin/python3
import random
import time

class Character:
	def __init__(self,attacks):
		self.hitpoints = 1000
		self.attack = random.randint(20,30)
		self.defense = random.randint(10,20)
		self.attacks = attacks
		self.items = set()
	def damage(self,hp):
		self.hitpoints -= hp
	def heal(self,h):
		self.hitpoints += h.hp
	def additem(self,item):
		self.items.add(item)

class Heart:
	def __init__(self,hp=30):
		self.hp = hp

heart = Heart()
superheart = Heart(60)
ultraheart = Heart(90)
maxheart = Heart(120)

player = Character(('SLASH', 'FIREBALL', 'ICE CRYSTAL'))
enemy = Character(('BITE', 'STOMP', 'SMASH'))
itemlist = ["HEART", "SUPER HEART", "ULTRA HEART", "MAX HEART"]
constantslash = random.randint(60, 100)
constantfireball = random.randint(60, 100)
constanticecrystal = random.randint(60, 100)
constantbite = random.randint(30, 70)
constantstomp = random.randint(30, 70)
constantsmash = random.randint(30, 70)
command = ''
damageslash = int((0.1 * (player.attack - enemy.defense) * constantslash) + 0.5)
damagefireball = int((0.1 * (player.attack - enemy.defense) * constantfireball) + 0.5)
damageicecrystal = int((0.1 * (player.attack - enemy.defense) * constanticecrystal) + 0.5)
damagebite = int((0.1 * (enemy.attack - player.defense) * constantbite) + 0.5)
damagestomp = int((0.1 * (enemy.attack - player.defense) * constantstomp) + 0.5)
damagesmash = int((0.1 * (enemy.attack - player.defense) * constantsmash) + 0.5)

def playerturn():
    command = input(string)
    print(command)
    while command not in ("ATTACK", "ITEMS", "FLEE"):
        print(errormessage)
        time.sleep(1)
        command = input(string)
    if command == "ATTACK":
        attack = input(attackstring)
        while attack not in player.attacks:
            print(errormessage)
            time.sleep(1)
            attack = input(attackstring)
        if attack == "SLASH":
            print("You swung your blade...")
            time.sleep(2)
            print("...and inflicted", damageslash, "damage to ENEMY!")
            enemy.damage(damageslash)
            time.sleep(1)
        elif attack == "FIREBALL":
            print("You hurled a fireball...")
            time.sleep(2)
            print("...and inflicted", damagefireball, "damage to ENEMY!")
            enemy.damage(damagefireball)
            time.sleep(1)
        elif attack == "ICE CRYSTAL":
            print("You chucked an icicle...")
            time.sleep(2)
            print("...and inflicted", damageicecrystal, "damage to ENEMY!")
            enemy.damage(damageicecrystal)
            time.sleep(1)
        return True
    elif command == "ITEMS":
        items = input(itemstring)
        while items not in itemlist:
            print(errormessage)
            time.sleep(1)
            items = input(itemstring)
        if items == "HEART":
            player.heal(heart)
            print(f"You restored {heart.hp} HP!")
            time.sleep(1)
        elif items == "SUPER HEART":
            player.heal(superheart)
            print(f"You restored {superheart.hp} HP!")
            time.sleep(1)
        elif items == "ULTRA HEART":
            player.heal(ultraheart)
            print(f"You restored {ultraheart.hp} HP!")
            time.sleep(1)
        elif items == "MAX HEART":
            player.heal(maxheart)
            print(f"You restored {maxheart.hp} HP!")
            time.sleep(1)
        if player.hitpoints > 1000:
            print("You're already at max HP!")
            player.hitpoints = 1000
            time.sleep(1)
        itemlist.remove(items)
        return True
    elif command == "FLEE":
        print("You ran away!")
        time.sleep(1)
        return False

def hpstatistics():
    print(f"ENEMY has {enemy.hitpoints}/1000 HP.")
    time.sleep(1)
    print(f"You currently have {player.hitpoints}/1000 HP.")
    time.sleep(1)

def enemyturn():
    print("ENEMY readies an attack!")
    time.sleep(1)
    enemychoice = random.choice(enemy.attacks)
    if enemychoice == "BITE":
        print("ENEMY latches its jaws onto you...")
        time.sleep(2)
        print("...and thus you received", damagebite, "damage!")
        player.damage(damagebite)
        time.sleep(1)
    elif enemychoice == "STOMP":
        print("ENEMY raises its foot onto you...")
        time.sleep(2)
        print("...and thus you received", damagestomp, "damage!")
        player.damage(damagestomp)
        time.sleep(1)
    elif enemychoice == "SMASH":
        print("ENEMY charges up to ram into you...")
        time.sleep(2)
        print("...and thus you received", damagesmash, "damage!")
        player.damage(damagesmash)
        time.sleep(1)

def defeatstate():
    if enemy.hitpoints <= 0:
        print("ENEMY is defeated!")
        time.sleep(1)
        print("YOU WIN!")
        time.sleep(2)
        print("You obtained 43 EXP.")
        time.sleep(1)
        return True
    elif player.hitpoints <= 0:
        print("You were defeated!")
        time.sleep(1)
        print("You lost the battle...")
        time.sleep(2)
        print("GAME OVER")
        time.sleep(1)
        return True
    else:
        return False

# Start battle
print("ENEMY attacks!")
time.sleep(1)
hpstatistics()
string = "Will you ATTACK, use ITEMS, or FLEE? "
errormessage = "Command not recognized. Try again."
attackstring = "Which attack will it be: SLASH, FIREBALL, or ICE CRYSTAL? "
itemstring = "Which item will you choose: HEART, SUPER HEART, ULTRA HEART, or MAX HEART? "
while True:
    if not playerturn():
        break
    if defeatstate():
        break
    enemyturn()
    if defeatstate():
        break
    hpstatistics()
