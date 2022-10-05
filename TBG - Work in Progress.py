import random #a module (file of prewritten code)

game_over = False
health = 100
room = 1
#---------------function for which monster appears----------
def monster(biome):
    num = random.randrange(0,100) # function call
    if biome == "Bedroom":
        if num < 20: # 20% percent chance 
            print("A zombie breaks out of the closet is running to attack you")
            BattleSystem("Zombie", health)
        elif num < 50: # 30% percent chance
            print("A skeleton crawls under the bed and tries to grab you")
            BattleSystem("Skeleton", health)
        elif num < 90: # 40% percent chance
            print("An ogre is slamming on your window and tries to get in")
            BattleSystem("Ogre", health)
        else: #10 percent chance
            print("You see big zombified rats charge at you from the floorboards")
            BattleSystem("Rats", health)
    elif biome == "Hallway":
        if num < 20: # 20% percent chance 
            print("A zombie is breaking into your window on the left")
        elif num < 50: # 30% percent chance
            print("A skeleton is aiming an arrow at you from the attic")
        elif num < 90: # 40% percent chance
            print("A giant spider bites you on your way out!")
        else: #10 percent chance
            print("A witch throws a potion at you from across the hallway and disappears")
    elif biome == "TopStair":
        if num < 25: # 25% percent chance 
            print("A zombie comes up from the floorboard trying to grab at you")
        elif num < 75: # 50% percent chance
            print("A witch comes out the bathroom and is heading towards you direction")
        elif num < 90: # 15% percent chance
            print("Spiders start flooding the hallway!")
        else: #10 percent chance
            print("Acid slime creature is oozing from the walls behind you")
#----------------End of monster appearance function-----------

#--------------Battle system Function-----------------------
def BattleSystem(monsterType, playerHealth):
    if monsterType == "Zombie":
        monsterHealth = 20
    elif monsterType == "Skeleton":
        monsterHealth = 40
    elif monsterType == "Ogre":
        monsterHealth = 30
    elif monsterType == "Rats":
        monsterHealth = 18
    
    
    while monsterHealth > 0 and playerHealth > 0:
        if monsterType == "Zombie":
            monsterAttack = random.randrange(8, 13)
        elif monsterType == "Skeleton":
            monsterAttack = random.randrange(6, 12)
        elif monsterType == "Ogre":
            monsterAttack = random.randrange(7, 10)
        elif monsterType == "Rats":
            monsterAttack = random.randrange(12, 20)
        print("The", monsterType, "attacks for", monsterAttack)
        playerHealth = playerHealth - monsterAttack
        print("Your health is now", playerHealth)
        
        
        playerAttack = random.randrange(5, 12)
        print("You attack for", playerAttack)
        monsterHealth = monsterHealth - monsterAttack
        print("The monster health is now", monsterHealth)
        
    if playerHealth == 0:
        print("You died to a", monsterType)
        game_over == True
    elif monsterHealth <= 0:
        print("You killed the", monsterType)
    print("Your current health is", playerHealth)
    
    return playerHealth


#---------------End of Battle system Function---------------

     
# Moving around (Map)
while game_over is not True:
    if room == 1:
        print()
        monster("Bedroom") #function call
        print("Your only direction you can go is (e)ast ")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
    if room == 2:
        print()
        monster("Hallway") #function call
        print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 1
        else:
            print("Sorry that isn't a direction you can go.")
    
    if room == 3:
        print()
        print("You are in the middle of the hallway. You can go (n)orth or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'North':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
            
    if room == 4:
        print()
        print("You are at the end of the hallway at the top of the stairway.")
        monster("TopStair") #function call
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        elif choice == 'placeholder':
            room = 10
        else:
            print("Sorry that isn't a direction you can go.")