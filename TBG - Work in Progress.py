
import random #Module for random number generator usage 






# Default settings when starting the game
game_over = False
room = 1
health = 100
inventory = {
    "bat": 0,
    "healthpot": 0,
    "double A": 0,
    "flashlight": 0,
    "map riddle": 0,
    }


#--------------Battle system Function-----------------------
def BattleSystem(monsterType):
    global health

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
    while monsterHealth > 0 and health > 0:


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
        health = health - monsterAttack
        print("Your health is now", health)
        
        
        
        #Base Damage
        playerAttack = random.randrange(5, 12)
        
        
        #Damage Change
        if "baseball ball" in inventory == 1:
            playerAttack = random.randrange(9,20)
        else:
            playerAttack = random.randrange(5, 12)
                 
                 
                 
        #Player Attacks
        monsterHealth = monsterHealth - monsterAttack
        print("You attack for", playerAttack)
        print("The monster health is now", monsterHealth)
        
        
    #Zero health = Game over
    if health <= 0:
        print("You died to a", monsterType)
        global game_over
        game_over = True
        
    elif monsterHealth <= 0:
        print("You killed the", monsterType)
    print("Your current health is", health)
#---------------End of Battle system Function---------------


#---------------function for which monster appears----------
def monster(biome):
    num = random.randrange(0,100) # randomize chances when function is called
    if biome == "Bedroom":
        if num < 20: # 20% percent chance 
            print("A zombie breaks out of the closet is running to attack you")
            BattleSystem("Zombie")
        elif num < 50: # 30% percent chance
            print("A skeleton crawls under the bed and tries to grab you")
            BattleSystem("Skeleton")
        elif num < 90: # 40% percent chance
            print("An ogre is slamming on your window and tries to get in")
            BattleSystem("Ogre")
        else: #10 percent chance
            print("You see big zombified rats charge at you from the floorboards")
            BattleSystem("Rats")
    elif biome == "Hallway":
        if num < 20: # 20% percent chance 
            print("A zombie is breaking into your window on the left")
            BattleSystem("Zombie")
        elif num < 50: # 30% percent chance
            print("A skeleton is aiming an arrow at you from the attic")
            BattleSystem("Skeleton")
        elif num < 90: # 40% percent chance
            print("A giant spider appears from the floorboards!")
            BattleSystem("Spider")
        else: #10 percent chance
            print("A witch is charging up to throw a potion at you.")
            BattleSystem("Witch")
    elif biome == "TopStair":
        if num < 25: # 25% percent chance 
            print("A zombie comes up from the floorboard trying to grab at you")
            BattleSystem("Zombie")
        elif num < 75: # 50% percent chance
            print("A witch comes out the bathroom and is heading towards you direction")
            BattleSystem("Witch")
        elif num < 90: # 15% percent chance
            print("Spiders start flooding the hallway!")
            BattleSystem("SSpider")
        else: #10 percent chance
            print("Acid slime creature is oozing from the walls behind you")
            BattleSystem("Slime")
#----------------End of monster appearance function-----------


#-------function to use health potion-------------------------
def healthpot():
    global health
    health += 30
    print("You used a health pot and recovered 30 hp. Your health is now", health)
    inventory["healthpot"] =- 1
    health < 101
    


#local game variables
room1Mon = False
room2Mon = False
#room3Mon = False   (Not used) 
room4Mon = False
room5Mon = False
room6Mon = False
room7Mon = False
room8Mon = False
room9Mon = False
room10Mon = False

#items default settings

bat = False
hpot1 = False
hpot2 = False
hpot3 = False
hpot4 = False
hpot5 = False
hpot6 = False
AAbatt = False
flashlight = False
riddle_map = False

     
# [Game starts]
   
#    Moving around the map   
#    User input that affects the game
while True:

    if (game_over):
        break

    #Bedroom
    if room == 1:
        print("You're in your bedroom ")
        if room1Mon == False:
            monster("Bedroom") #function call
            if (game_over):
                break
            room1Mon = True
        print()
        print("A direction you can go is (e)ast")
        if bat == False:
            print("and you see a baseball bat close to the door")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        elif (choice == 'baseball bat' or choice == 'pick up baseball bat' or choice == 'bat')  and bat == False:
            inventory["bat"] += 1 #baseball bat for more dmg
            bat = True
            print("You picked up the bat, now you do more damage")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry, that is not an option.")
            
    #Hallway next to bedroom
    elif room == 2: 
        print()
        if room2Mon == False:
            monster("Hallway") #function call
            if (game_over):
                break
            room2Mon = True
            print("You see a magical health potion on the floor.")
            print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 1
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot1 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot1 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp. (Warning: You can only use it in levels where you picked it up")
        elif choice == 'use health pot':
            healthpot()
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry, that is not an option.")
    
    #Middle of hallway
    elif room == 3:
         
        print()
        print("You are in the middle of the hallway. You can go (n)orth or (s)outh ")
        print("You see double A batteries on the floor.")
        choice = input()
        if choice == ('double A batteries' or choice == 'pick up double A batteries') and AAbatt == False:
            inventory["Double A Batteries"] += 1 #Double A batteries for flashlight
            AAbatt = True
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'North':
            room = 2
        else:
            print("Sorry that isn't a direction you can go.")
            
    #End of hallway        
    elif room == 4:
         
        print()
        print("You are at the end of the hallway at the top of the stairway. The stairway is on your left")
        if room4Mon == False:
            monster("TopStair") #function call
            if (game_over):
                break
            room4Mon = True
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        elif choice == 'e' or choice == 'e' or choice == 'East':
            room = 5
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot2 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot2 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that isn't a direction you can go.")
    
    #Bottom of stairway
    elif room == 5:
         
        print()
        print("You're at the bottom of the stairway and the door to leave is to your right")
        print("A magical health potion rolls around the corner from the shoe rack")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'West':
            room = 4
        elif choice == 's' or choice == 's' or choice == 'South':
            room = 6
        else:
            print("Sorry that isn't a direction you can go.")
            
    #Outside with house door behind
    elif room == 6:
         
        print()
        print("You're outside, you can go (w)est, (n)orth, (e)ast, (s)outh")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 5
            
        elif choice == 'w' or choice == 'W' or choice == 'West':
            print("Game over! You died by: ")
            game_over = True
        elif choice == 'e' or choice == 'E' or choice == 'West':
            print("Game over! You died by: ")
            game_over = True
            
        #The room you're supposed to go into
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 7
        else:
            print("Sorry that isn't a direction you can go.")

    #In the forest with the neighborhood behind
    elif room == 7:
         
        print()
        print("You're in a very overgrown forest, you can go (w)est, (n)orth, (e)ast, (s)outh")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 6
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 8
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "W1"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = "E1"
        else:
            print("Sorry that isn't a direction you can go.")
    #Middle of the Forest
    elif room == 8:
         
        print()
        print("You find yourself in the middle of the forest with the least amount of trees, you can go (w)est, (n)orth, (e)ast, (s)outh")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 9
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "W2"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = "E2"
        else:
            print("Sorry that isn't a direction you can go.")
    #Very south of the Forest    
    elif room == 9:
         
        print()
        print("The trail takes a rigid turn to the left.")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 8
        elif choice == 'e' or choice == 'e' or choice == 'e':
            room = 10
        elif choice == 'w' or choice == 'w' or choice == 'West':
            room = "W3"
        else:
            print("Sorry that isn't a direction you can go.")
    #Southeast of the Forest    
    elif room == 10:
         
        print()
        print("At this point in the trail, you've stopped in your tracks and see two other paths, one in front of you, the other to your right.")

        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'West':
            room = 9
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = 11
        elif choice == 'n' or choice == 'N' or choice == 'North':
            room = "E2"
        elif choice == 's'or choice == 'S' or choice == 'South':
            room = 12
        else:
            print("Sorry that isn't a direction you can go.")
    #The room right before the good ending
    elif room == 11:
         
        print()
        print("In the distance you see what looks to be red bricks of a building with multiple barbed wires surrounding it. Do you wish to continue going down this path? (Y/N): ")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'no' or choice == "No":
            room = 10
        elif choice == 'y' or choice == 'Y' or choice == 'yes' or choice == "Yes":
            print("Placeholder: Win")
            game_over = True
        else:
            print("Sorry that isn't a direction you can go.")
    #Room that will fake out player leading them to losing
    elif room == 12:
         
        print()
        print("Room 12")
 
        choice = input("You hear sounds of people talking with laughter and a bright yellow light from the same direction. Do you wish to continue going down this path? (Y/N): ")
        if choice == 'n' or choice == 'N' or choice == 'no' or choice == "No":
            room = 10
        elif choice == 'y' or choice == 'Y' or choice == 'yes' or choice == "Yes":
            print("Placeholder: Lose")
            game_over = True
        else:
            print("Sorry that isn't a direction you can go.")
            
            
            
            
            
    #-----------------------The extra rooms in the forest-----------------------
    #Northwest of Forest
    elif room == "W1":
         
        print()
        print("W1")
        monster("") #function call
        if (game_over):
                break
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'East':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = "W2"
        else:
            print("Sorry that isn't a direction you can go.")
    #West of Forest
    elif room == "W2":
         
        print()
        print("W2")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "W1"
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = 8
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = "W3"
        else:
            print("Sorry that isn't a direction you can go.")
    #Southwest of Forest
    elif room == "W3":
         
        print()
        print("W3")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "W2"
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "9"
        else:
            print("Sorry that isn't a direction you can go.")
    #Northeast of Forest
    elif room == "E1":
         
        print()
        print("E1")
        
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'West':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = "E2"
        else:
            print("Sorry that isn't a direction you can go.")
    #East of Forest
    elif room == "E2":
         
        print()
        print("E2")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "E1"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 8
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 10
        else:
            print("Sorry that isn't a direction you can go.")

print("Game over")
