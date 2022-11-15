#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Samuel Jung and Tristan Degen
#The game that we created is a pokemon game where you select one pokemon and the computer selects one and you can select different types of attacks in an attenpt to defeat your opponenets pokemon
#Pokemon 

import random #Python Random module is an in-built module of Python which is used to generate random numbers
import time #The time function allows functionality like getting the current time, pausing the Program from executing

Pokemon = ["Charmander","Bulbasaur","Squirtle"]#List of Pokemon
Charmander_attacks = {"dragon breath":"83",
                      "fire fang":"90",
                      "flamethrower":"65"} #Dictionary of Charmander's attacks 
Bulbasaur_attacks = {"razor leaf":"80",
                      "poison powder":"87",
                      "leech seed":"58"} #Dictionary of Bulbasaur's attacks
Squirtle_attacks = {"shell smash":"115",
                      "aqua tail":"92",
                      "hydro pump":"108"} #Dictionary of Squirtle's attacks

user_health = 0 #user health before selecting a pokemon
comp_health = 0 #computer health before selecting a pokemon
user_turn = 3 #amount of turns the user had 
comp_turn = 3 #amount of turns the computer has 

print("Sam : Welcome to Pokemon. My name is Sam and I introduce new lvl.1 trainers to the game.") #print statement
time.sleep(4) #Python time sleep() function suspends execution for the given number of seconds.
print("Sam : In this game, you will clash against fellow pokemon trainers and see who is victorious") #print statement
time.sleep(4) #Python time sleep() function suspends execution for the given number of seconds.
print("Sam : Don't worry, you won't face off against strong pokemon trainers. Only against other lvl.1 trainers") #print statement
time.sleep(4) #Python time sleep() function suspends execution for the given number of seconds.
print("Sam : Speak of the devil... it looks like Ash wants to have a go with you and your pokemons") #print statement
time.sleep(4) #Python time sleep() function suspends execution for the given number of seconds.
print("Sam : Well I'll leave you guys to it.") #print statement
time.sleep(3) #Python time sleep() function suspends execution for the given number of seconds.
print("Ash : It looks like your new here. Well get ready because I am not! MUHUHAHAHA") #print statement
time.sleep(4) #Python time sleep() function suspends execution for the given number of seconds.
print("             FIGHT         ") #print statement



Comp_Pok = random.choice(Pokemon) #Computer randomly selects a pokemon 

if Comp_Pok == "Charmander":
    comp_health += 282 #amount of health computer has if it selects Charmander
elif Comp_Pok == "Bulbasaur":
    comp_health += 294 #amount of health computer has if it selects Bulbasaur 
elif Comp_Pok == "Squirtle":
    comp_health += 198 #amount of health computer has if it selects Squirtle
print(f"Your opponent, Ash, chose " + Comp_Pok) #print statement stating what pokemon the computer randomly selected





print(f"Choose a pokemon to fight back against " + Comp_Pok + "!") #print statement stating what pokemon you selected
print("These are your pokemons you can choose from: Charmander, Bulbasaur, Squirtle") #print statement
User_Pok = input("Who do you choose ? : ") #you would input what pokemon you select here
User_Pok = User_Pok.upper() #.upper returns a string where all characters are in upper case

if User_Pok == "CHARMANDER": #if you select Charmander it activate print statement below
    print("You choose Charmander!") #print statement
    user_health += 282 #amount of health you have if you select Charmander
elif User_Pok == "BULBASAUR": #if you select Bulbasaur it wit activate print statement below
    print("You choose Bulbasaur!") #print statement
    user_health += 294 #amount of health you have if you select Bulbasaur
elif User_Pok == "SQUIRTLE": #if you select Squirtle it wit activate print statement below
    print("You choose Squirtle!") #print statement
    user_health += 198 #amount of health you have if you select Squirtle
else:
    print("You don't have that pokemon but don't worry...") #print statement
    User_Pok = random.choice(Pokemon).upper() #selects pokemon at random due to an invalid input 
    print(f"It looks like " + User_Pok + " came out of it's pokeball to fight for you!") #print statement stating random pokemon that was given to you
    if User_Pok == "CHARMANDER": #if Charmander is chosen it will activate statment below
        user_health += 282 #amount of health you have if computer selects Charmander
    elif User_Pok == "BULBASAUR": #if Bulbasaur is chosen it will activate statment below
        user_health += 294 #amount of health you have if computer selects Bulbasaur
    elif User_Pok == "SQUIRTLE": #if Squirtle is chosen it will activate statment below
        user_health += 198 #amount of health you have if computer selects Squirtle






print("Choose an attack for your pokemon!")
if User_Pok == "CHARMANDER": #if Charmander is chosen it will activate statment below
    Atk_opt = str(list(Charmander_attacks.keys())) #The .keys method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python.
if User_Pok == "BULBASAUR": #if Bulbasaur is chosen it will activate statment below
    Atk_opt = str(list(Bulbasaur_attacks.keys())) #The .keys method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python.
if User_Pok == "SQUIRTLE": #if Squirtle is chosen it will activate statment below
    Atk_opt = str(list(Squirtle_attacks.keys())) #The .keys method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python.
print(f"These are the attacks your pokemon can do: " + Atk_opt) #print statement connected to the .keys which prints the print statement and the .keys function together





while comp_turn != 0 and user_health >= 0 and comp_health >= 0: #does actions below if computer turn isnt equal to 0, user health is greater or equal to 0 and computer health is greater or equal to 0

    UAtk_1 = input("What do you choose: ").lower() #the .lower method returns the lowercase string from the given string. It converts all uppercase characters to lowercase.
    if UAtk_1 in list(Charmander_attacks.keys()): #If the attack matches a key in the Charmander_attacks dictionary lines below are activated
        print(f"You chose " + UAtk_1.upper() + " !") #print statement which states the attack chosen
        u1atk_damage = int(Charmander_attacks.get(UAtk_1)) #damage you inflict on computer due to attack
    elif UAtk_1 in list(Bulbasaur_attacks.keys()): #If the attack matches a key in the Bulbasaur_attacks dictionary lines below are activated
        print(f"You chose " + UAtk_1.upper() + " !") #print statement which states the attack chosen
        u1atk_damage = int(Bulbasaur_attacks.get(UAtk_1)) #damage you inflict on computer due to attack
    elif UAtk_1 in list(Squirtle_attacks.keys()): #If the attack matches a key in the Squirtle_attacks dictionary lines below are activated 
        print(f"You chose " + UAtk_1.upper() + " !") #print statement which states the attack chosen
        u1atk_damage = int(Squirtle_attacks.get(UAtk_1)) #damage you inflict on computer due to attack
    else:
        print(f"You don't have that attack but don't worry, " + User_Pok + " will choose an attack himself...") #print statement stating what attack the computer chose for you at random 
        if User_Pok == "CHARMANDER": #if user selected Charmander lines below are activated
            UAtk_1 = random.choice(list(Charmander_attacks.keys())) #computer chooses random attack from dictionary for an invalid input
            print(f"It looks like " + User_Pok + " is going to use " + UAtk_1 + " !") #print statement stating what attack was chosen for you
            u1atk_damage = int(Charmander_attacks.get(UAtk_1)) #damage that Charmader inflicts on computer taken from attack in Charmander_attacks dictionary
        elif User_Pok == "BULBASAUR": #if user selected Bulbasaur lines below are activated
            UAtk_1 = random.choice(list(Bulbasaur_attacks.keys())) #computer chooses random attack from dictionary for an invalid input
            print(f"It looks like " + User_Pok + " is going to use " + UAtk_1 + " !") #print statement stating what attack was chosen for you
            u1atk_damage = int(Bulbasaur_attacks.get(UAtk_1)) #damage that Bulbasaur inflicts on computer taken from attack in Bulbasaur_attacks dictionary
        elif User_Pok == "SQUIRTLE": #if user selected Squirtle lines below are activated
            UAtk_1 = random.choice(list(Squirtle_attacks.keys())) #computer chooses random attack from dictionary for an invalid input
            print(f"It looks like " + User_Pok + " is going to use " + UAtk_1 + " !") #print statement stating what attack was chosen for you
            u1atk_damage = int(Squirtle_attacks.get(UAtk_1)) #damage that Squirtle inflicts on computer taken from attack in Squirtle_attacks dictionary

    comp_health -= u1atk_damage #subtracts computers attack from user health
    user_turn -= 1 #subract a move from the computer
    print(f"Now Ash's " + Comp_Pok + " is at " + str(comp_health) + " hp right now!") #print statement stating the name of your pokemon and its health


    if user_health <= 0: #if user health is below or equal to 0 it prints the print statement below
        print("                  YOU LOSE                ") #print statement
        print("Ash: Too Bad Sucker! I will admit, you were a tough match but it sucks to suck! HAHAHA") #print statement
        break #breaks out of loop early if condition is met
    elif comp_health <= 0: #if computer health is below or equal to 0 it prints the print statement below
        print("                  YOU WIN!                ") #print statement
        print("Ash: Damn it! I will beat you the next time we face off against each other! Grrrrrr...") #print statement
        break #breaks out of loop early if condition is met
    elif comp_turn == 0: #if computer turn is equal to zero it will print the print statement below
        print("It looks like both of your pokemons are too tired to fight. Draw!") #print statement
        break #breaks out of loop early if condition is met



    print("Now it's Ash's turn! What will he choose?") #print statement 
    time.sleep(6) #Python time sleep() function suspends execution for the given number of seconds.
    if Comp_Pok == "Charmander":
        CAtk_1 = random.choice(list(Charmander_attacks.keys())) #computer randomly selects attack from Charmander_attacks dictionary
        print(f"Ash chose " + CAtk_1 + " !") #print statement stating what attack the computer chose to attack you with
        c1atk_damage = int(Charmander_attacks.get(CAtk_1)) #damage that Charmander inflicts on user taken from attack in Charmander_attacks
    elif Comp_Pok == "Bulbasaur":
        CAtk_1 = random.choice(list(Bulbasaur_attacks.keys())) #computer randomly selects attack from Bulbasaur_attacks dictionary
        print(f"Ash chose " + CAtk_1 + " !") #print statement stating what attack the computer chose to attack you with
        c1atk_damage = int(Bulbasaur_attacks.get(CAtk_1)) #damage that Charmander inflicts on user taken from attack in Bulbasaur_attacks
    elif Comp_Pok == "Squirtle":
        CAtk_1 = random.choice(list(Squirtle_attacks.keys())) #computer randomly selects attack from Squirtle_attacks dictionary
        print(f"Ash chose " + CAtk_1 + " !") #print statement stating what attack the computer chose to attack you with
        c1atk_damage = int(Squirtle_attacks.get(CAtk_1)) #damage that Squirtle inflicts on user taken from attack in Squirtle_attacks

    user_health -= c1atk_damage #subtracts computers attack from user health
    comp_turn -=1 #subract a move from the computer
    print(f"Now your " + User_Pok + " is at " + str(user_health) + " hp right now!") #print statement stating the name of your pokemon and its health

else:
    if user_health <= 0: #if user health is below or equal to 0 it prints the print statement below
        print("You Lose") #print statement
        print("Ash: Too Bad Sucker! I will admit, you were a tough match but it sucks to suck! HAHAHA") #print statement
    elif comp_health <= 0: #if computer health is below or equal to 0 it prints the print statement below
        print("You Win!") #print statement
        print("Ash: Damn it! I will beat you the next time we face off against each other! Grrrrrr...") #print statement
    elif comp_turn == 0: #if computer turn is equal to zero it will print the print statement below
        print("It looks like both of your pokemons are too tired to fight. Draw!") #print statement
 



