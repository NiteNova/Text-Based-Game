import random #a module (file of prewritten code)



game_over = False
room = 1

#variables, lists, etc for player
inventory = []
health = 100
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
            BattleSystem("Zombie", health)
        elif num < 50: # 30% percent chance
            print("A skeleton is aiming an arrow at you from the attic")
            BattleSystem("Skeleton", health)
        elif num < 90: # 40% percent chance
            print("A giant spider appears from the floorboards!")
            BattleSystem("Spider", health)
        else: #10 percent chance
            print("A witch is charging up to throw a potion at you.")
            BattleSystem("Witch", health)
    elif biome == "TopStair":
        if num < 25: # 25% percent chance 
            print("A zombie comes up from the floorboard trying to grab at you")
            BattleSystem("Zombie", health)
        elif num < 75: # 50% percent chance
            print("A witch comes out the bathroom and is heading towards you direction")
            BattleSystem("Witch", health)
        elif num < 90: # 15% percent chance
            print("Spiders start flooding the hallway!")
            BattleSystem("SSpider", health)
        else: #10 percent chance
            print("Acid slime creature is oozing from the walls behind you")
            BattleSystem("Slime", health)
#----------------End of monster appearance function-----------

#--------------Battle system Function-----------------------
def BattleSystem(monsterType, playerHealth):
    # All enemy types
    if monsterType == "Zombie":
        monsterHealth = 20
    elif monsterType == "Skeleton":
        monsterHealth = 40
    elif monsterType == "Ogre":
        monsterHealth = 30
    elif monsterType == "Rats":
        monsterHealth = 18
    elif monsterType == "Spider":
        monsterHealth = 16
    elif monsterType == "Witch":
        monsterHealth = 20
    elif monsterType == "Slime":
        monsterHealth = 19
    elif monsterType == "SSpider":
        monsterHealth = 18
        
        
    #Actually battling 
    while monsterHealth > 0 and playerHealth > 0:
        if monsterType == "Zombie":
            monsterAttack = random.randrange(8, 13)
        elif monsterType == "Skeleton":
            monsterAttack = random.randrange(6, 12)
        elif monsterType == "Ogre":
            monsterAttack = random.randrange(7, 10)
        elif monsterType == "Rats":
            monsterAttack = random.randrange(12, 20)
        elif monsterType == "Spider":
            monsterAttack = random.randrange(10, 16)
        elif monsterType == "Witch":
            monsterAttack = random.randrange(8, 13)
        elif monsterType == "Slime":
            monsterAttack = random.randrange(9, 14)
        elif monsterType == "SSpider":
            monsterAttack = random.randrange(12, 20)
        
        #Enemy attacks    
        print("The", monsterType, "attacks for", monsterAttack)
        playerHealth = playerHealth - monsterAttack
        print("Your health is now", playerHealth)
        
        #Damgae Change
        for i in range(len(inventory)):
            if inventory[i] == "baseball bat":
                playerAttack = random.randrange(9,20)
            else:
                 playerAttack = random.randrange(5, 12)
        #Player Attacks
        print("You attack for", playerAttack)
        monsterHealth = monsterHealth - monsterAttack
        print("The monster health is now", monsterHealth)
        
    #Death = Game over
    if playerHealth == 0:
        print("You died to a", monsterType)
        game_over == True
        
    elif monsterHealth <= 0:
        print("You killed the", monsterType)
    print("Your current health is", playerHealth)
    
    return playerHealth


#---------------End of Battle system Function---------------

#local game variables
room1Mon = False
bat = False
     
# Moving around (Map)
while game_over is not True:
    if room == 1:
        print()
        print("You're in your bedroom ")
        if bat == False:
            print("and you see a baseball bat close to the door")
        if room1Mon == False:
            monster("Bedroom") #function call
            room1Mon = True
        print("A direction you can go is (e)ast) ")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        elif (choice == 'baseball bat' or choice == 'pick up baseball bat') and bat == False:
            inventory.append("Baseball bat")
            bat = True
        elif choice == 'inventory':
            print(inventory)
        else:
            print("Sorry, that is not an option.")
    if room == 2:
        print()
        monster("Hallway") #function call
        print("You see a magical health potion on the floor")
        print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 1
        elif choice == 'magical health potion' or choice == 'pick up health magical potion':
            inventory.append("Health Magical Potion")
        else:
            print("Sorry, that is not an option.")
    
    if room == 3:
        print()
        print("You are in the middle of the hallway. You can go (n)orth or (s)outh ")
        print("You see double A batteries on the floor.")
        choice = input()
        if choice == 'double A batteries' or choice == 'pick up double A batteries':
            inventory.append("Double A Batteries")
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
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        elif choice == 'e':
            room = 5
        else:
            print("Sorry that isn't a direction you can go.")
    
    if room == 5:
        print()
        print("You're at the bottom of the stairway and the door to leave is to your right")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 4
        elif choice == '':
            room = 6
        else:
            print("Sorry that isn't a direction you can go.")
            
    if room == 6:
        print()
        print("You're outside, you can go (w)est, (n)orth, (e)ast, (s)outh")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 5
        elif choice == '':
            room = 7
        else:
            print("Sorry that isn't a direction you can go.")

    if room == 7:
        print()
        print("You're in a forest, you can go (w)est, (n)orth, (e)ast, (s)outh")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 6
        elif choice == '':
            room = 8
        else:
            print("Sorry that isn't a direction you can go.")

    if room == 8:
        print()
        print("You're near the end of the forest and see a light in the distance, you can go (w)est, (n)orth, (e)ast, (s)outh")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 7
        elif choice == '':
            room = 9
        else:
            print("Sorry that isn't a direction you can go.")
        
    if room == 9:
        print()
        print("")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 8
        elif choice == '':
            room = 10
        else:
            print("Sorry that isn't a direction you can go.")
        
    if room == 10:
        print()
        print("")
        monster("") #function call
        choice = input()
        if choice == '' or choice == '' or choice == '':
            room = 9
        elif choice == '':
            room = 10
        else:
            print("Sorry that isn't a direction you can go.")
