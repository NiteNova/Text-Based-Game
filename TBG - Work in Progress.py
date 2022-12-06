import timer
import random #Module for random number generator usage 






# Default settings when starting the game
game_over = False
room = 0
health = 100
inventory = {
    "bat": 0,
    "healthpot": 0,
    "double A": 0,
    "flashlight": 0,
    "map riddle": 0,
    }


#------------Battle system function-------------------
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
        if inventory["bat"] >= 1:
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
        
    elif monsterHealth <= 0 and health > 0:
        print("You killed the", monsterType)
    print("Your current health is", health)
    
#------------End of Battle system Function------------


#------------Monster appearing function-------
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
    elif biome == "Forest":
        if num < 35: # 35% percent chance 
            print("A zombie fell out of a tree making you think it's dead, but once your back is turned you hear it's sprinting at you. ")
            BattleSystem("Zombie")
        elif num < 55: # 20% percent chance
            print("A witch creeps from behind a tree and after being spotted, charges at you.")
            BattleSystem("Witch")
        elif num < 75: # 20% percent chance
            print("A giant spider jumps out of the bush towards your direction.")
            BattleSystem("SSpider")
        else: #25 percent chance
            print("Slime oozes from beneath the tree you're standing next to.")
            BattleSystem("Slime")
#------------End of monster appearance function-------


#------------Health potion function-------------------
def healthpot():
    global health
    if health < 100:
        health += 30
    if health > 100:
        health = 100
    print("You used a health pot and recovered 30 hp. Your health is now", health)
#------------End of health potion function------------



#local game variables
room1Mon = False
room2Mon = False 
room4Mon = False
room9Mon = False


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
chargflash = False
riddle_map = False

     
# [Game starts]
   
#    Moving around the map   
#    User input that affects the game
while True:
    if room == 0:
        print("Placeholder Story Desc")
        print()
        k = input("Enter any key to continue\n")
        if k == "k":
            room = 1
        else:
            room = 1

    #Bedroom
    if room == 1:
        print("You're in your bedroom and it's been hours since you've left it.")
        if room1Mon == False:
            monster("Bedroom") #Enemy function call (calls the battle system function)
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
        print("You are in the hallway, you can go (w)est to go back to your room or (s)outh ")
        if room2Mon == False:
            monster("Hallway") #Enemy function call (calls the battle system function)
            if (game_over):
                break
            room2Mon = True
            if hpot1 == False:
                print("You see a magical health potion on the floor.")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 1
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot1 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot1 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp. (Warning: You can only use it in areas that you picked it up in.")
        elif choice == 'use health pot' and hpot1 == True and inventory["healthpot"] <= 1:
            if inventory["healthpot"] >= 1:
                healthpot()
                inventory["healthpot"] -= 1
            else:
                print("Sorry mate, you aint got no more health potions right now.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry, that is not an option.")
    
    #Middle of hallway
    elif room == 3:
         
        print()
        print("You are in the middle of the hallway. You can go (n)orth or (s)outh ")
        if AAbatt == False:
            print("You see Double A batteries on the floor.")
        choice = input()
        if choice == ('Double A batteries' or choice == 'pick up Double A batteries') and AAbatt == False:
            inventory["double A"] += 1 #Double A batteries for flashlight
            print("You picked up the double A batteries")
            AAbatt = True
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'North':
            room = 2
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
            
    #End of hallway        
    elif room == 4:
         
        print()
        print("You are at the end of the hallway at the top of the stairway. The stairway is on your left")
        if room4Mon == False:
            monster("TopStair") #Enemy function call (calls the battle system function)
            if (game_over):
                break
            room4Mon = True
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 3
        elif choice == 'e' or choice == 'e' or choice == 'East':
            room = 5
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    
    #Bottom of stairway
    elif room == 5:
         
        print()
        print("You're at the bottom of the stairway. The path to the rest of the house is blocked off by a lot of debris and knocked down furniture. The door to leave is to your right")
        if hpot2 == False:
            print("A magical health potion rolls around the corner from the shoe rack and hit your shoes.")
        if flashlight == False:
            print("You also notice a flashlight on the floor.")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'West':
            room = 4
        elif choice == 's' or choice == 's' or choice == 'South':
            room = 6
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot2 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot2 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp. (Warning: You can only use it in areas that you picked it up in.")
        elif choice == 'use health pot' and hpot2 == True and inventory["healthpot"] <= 1:
            if inventory["healthpot"] >= 1:
                healthpot()
                inventory["healthpot"] -= 1
            else:
                print("Sorry mate, you aint got no more health potions right now.")
        elif choice == ('flashlight' or choice == 'pick up flashlight' or choice == 'Flashlight') and flashlight == False:
            print("You picked up the flashlight, now you need some batteries to charge it. (Command to put in batteries 'flashlight double A batteries') ")
            inventory["flashlight"] += 1
            flashlight = True
        elif choice == "flashlight double A batteries" and flashlight == True and AAbatt == True and chargflash == False:
            print("You put the double A batteries into the flashlight and instantly blinds you with the blinding light")
            chargflash = True
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
            
    #Outside with house door behind
    elif room == 6:
        print()
        print("You're outside and in front of you is a road and across the street there is a path to the forest. You can go (w)est, (n)orth, (e)ast, (s)outh")
        if chargflash == False:
            print("You went straight outside without any light and fell to your death into a nearby ditch full of monsters.")
            break
        if riddle_map == False:
            print("You see the map on the ground.")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 5
            
        elif choice == 'w' or choice == 'W' or choice == 'West':
            print("You died by a car explosion while walking down the road")
            break
        elif choice == 'e' or choice == 'E' or choice == 'West':
            print("You died after getting piled on by a huge group of zombies")
            break
        elif choice == 'map' or choice == "pick up map" and riddle_map == False:
            print("You picked up a map riddle, but it is blurred with a caption saying it only works once you're in the forest.")
            inventory["map riddle"] += 1
            riddle_map = True
        elif choice == 'inventory':
            print("You're carrying,", inventory)
            
        #The room you're supposed to go into
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 7
        else:
            print("Sorry that is not an option")

    #In the forest with the neighborhood behind
    elif room == 7:
         
        print()
        print("You're in a very overgrown forest, it gives you an eerie feeling. You can go (w)est, (n)orth, (e)ast, (s)outh")
        if hpot3 == False:
            print("A magical health potion can be seen in the mud.")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 6
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 8
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "W1"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = "E1"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot3 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot3 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp. (Warning: You can only use it in areas that you picked it up in.")
        elif choice == 'use health pot' and hpot3 == True and inventory["healthpot"] <= 1:
            if inventory["healthpot"] >= 1:
                healthpot()
                inventory["healthpot"] -= 1
            else:
                print("Sorry mate, you aint got no more health potions right now.")
        else:
            print("Sorry that is not an option")
    #Middle of the Forest
    elif room == 8:
         
        print()
        print("You find yourself in the middle of the forest with less trees than the rest of the forest, you can go (w)est, (n)orth, (e)ast, (s)outh")
        if room9Mon == False:
            monster("MidForest") #Enemy function call (calls the battle system function)
            if (game_over):
                break
            Room9Mon = True
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 9
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "W2"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = "E2"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    #Very south of the Forest    
    elif room == 9:
         
        print()
        print("You see the trail takes a rigid turn to the left at where you are right now.")
        if hpot4 == False:
            print("A shiny red magical health potion illuminates on the side the trail.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = 8
        elif choice == 'e' or choice == 'e' or choice == 'e':
            room = 10
        elif choice == 'w' or choice == 'w' or choice == 'West':
            room = "W3"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        elif (choice =='magical health potion' or choice == 'pick up health magical potion' or choice == 'health potion' or choice == 'health pot') and hpot4 == False:
            inventory["healthpot"] += 1 #Health pot for hp
            hpot4 = True
            print("You picked up an health potion, type 'use health pot' to recover missing hp. (Warning: You can only use it in areas that you picked it up in.")
        elif choice == 'use health pot' and hpot4 == True and inventory["healthpot"] <= 1:
            if inventory["healthpot"] >= 1:
                healthpot()
                inventory["healthpot"] -= 1
            else:
                print("Sorry mate, you aint got no more health potions right now.")
        else:
            print("Sorry that is not an option")
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
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    #The room right before the good ending
    elif room == 11:
         
        print()
        print("In the distance you see what looks to be red bricks of a building with multiple barbed wires surrounding it. Do you wish to continue going down this path? (Y/N): ")

        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'no' or choice == "No":
            room = 10
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'y' or choice == 'Y' or choice == 'yes' or choice == "Yes":
            print("Upon making your way towards the red building, a voice demands you to stop in your tracks and state your purpose.\nYou shout that you're a survivor and seeking for help. A painted door to look like part of the brick walls is opened and someone whispers to come in.\nThere you found safety and a group of other survivors. TO BE CONTINUED") 
            break
        else:
            print("Sorry that is not an option")
    #Room that will fake out player leading them to losing
    elif room == 12:
         
        print()
        choice = input("You hear sounds of people talking with laughter and a bright yellow light from the same direction. Do you wish to continue going down this path? (Y/N): ")
        if choice == 'n' or choice == 'N' or choice == 'no' or choice == "No":
            room = 10
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'y' or choice == 'Y' or choice == 'yes' or choice == "Yes":
            print("Continuing down this path had made you realize the noises and light were all hallucinations due to the low visible psychedelic fog.\nThis fog has also attracted a lot of the monsters leading them cornering you to your death.")
            break
        else:
            print("Sorry that is not an option")
            
            
            
            
            
    #-----------------------The extra rooms in the forest-----------------------
    #Northwest of Forest
    elif room == "W1":
         
        print()
        print("You went west and off from the trail of the forest")
        monster("Forest") #Enemy function call (calls the battle system function)
        if (game_over):
                break
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'East':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = "W2"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is fake and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    #West of Forest
    elif room == "W2":
         
        print()
        print("You went west and off from the trail of the forest")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "W1"
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = 8
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = "W3"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    #Southwest of Forest
    elif room == "W3":
         
        print()
        print("You went west and off from the trail of the forest")
        
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "W2"
        elif choice == 'e' or choice == 'E' or choice == 'East':
            room = "9"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
    #Northeast of Forest
    elif room == "E1":
         
        print()
        print("You went east and off from the trail of the forest")
        
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'West':
            room = 7
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = "E2"
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
            
        else:
            print("Sorry that is not an option")
    #East of Forest
    elif room == "E2":
         
        print()
        print("You went east and off from the trail of the forest")
        monster("Forest") #Enemy function call (calls the battle system function)
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North':
            room = "E1"
        elif choice == 'w' or choice == 'W' or choice == 'West':
            room = 8
        elif choice == 's' or choice == 'S' or choice == 'South':
            room = 10
        elif choice == 'map' or choice == 'use map' and riddle_map == True:
            print("Life has two choices, one is an illusion, the other is the brutal reality. Determine what is an illusion and what is real.")
        elif choice == 'inventory':
            print("You're carrying,", inventory)
        else:
            print("Sorry that is not an option")
print()
print("Game over")
