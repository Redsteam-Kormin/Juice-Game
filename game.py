#PLEASE INSTALL TERMCOLOR!
import os, sys, time, random
from os import system
from time import sleep as s
from termcolor import colored as c
from functions import *
from acheivements import *

#to anyone trying to fix/modify my code, have fun, i'm so bad at ts I hate looking at my own code.

badstuff = 0
rank = "Unrecognizable Brewery."
name = "The Nothing Brewery"
something = "Nothing"
money = 0
juices = ["Apple Juice"]
mpd = 0
juicecosts = [random.randint(1,5)]
preday = 0
day = 0
action = "b"
mp = 100
moneyextra = 1
mpchange = 0
selljuice = -1
foundjuice = 0
juicecount = 1
badmoney = 1
drinks = 0
mmy = 0
luck = random.randint(1,25)
superlucky = random.randint(1,100)
fruits = ["Green Apple", "Grape", "Mango", "Pineapple", "Orange", "Peach", "Lemon","Lime"]
superfruits = ["Golden Apple", "Gemmy Grape", "67 Mango", "Big Pineapple", "Tangerine", "Apricot", "Pink Lemon", "Key Lime"]

#Brewery Upgrade Variables
brewlevel = 0
fundcosts = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
brewmultiplier = [1,2,4,8,16,32,64]

#acheivements are now in acheivements.py

clear() #cool title card time
print(",-_/                ,---.       ")
print("'  | . . . ,-. ,-.  |  -'  ,-. ,-,-. ,-.")
print("   | | | | |   |-'  |  ,-' ,-| | | | |-'")
print("   | `-^ ' `-' `-'  `---|  `-^ ' ' ' `-'")
print("/` |                 ,-.|               ")
print("`--'                 `-+'            ")   
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('     "The game where you brew juice."')
print("") #VVV Ask for Brewery Name VVV
print("Your brewery will be named 'The [insert thing here] Brewery'.")
something = str(input("What will your brewery be called? "))
name = f"The {something} Brewery"

#begin game.
while 1:
    #reset money per day
    mpd = 0
    for x in juicecosts:
        mpd += x
        mpd == mpd*brewmultiplier
    if mp > 100: 
        mp = 100
    moneyextra = 1
    mpchange = 0
    preday = day
    clear()
    print("~~~~++++~~~~++++~~~~")
    print(name)
    print("Rank: ", rank)
    print("Brewery Level: ", brewlevel)
    print("Next Upgrade Cost: ", fundcosts[brewlevel])
    print("~~~~++++~~~~++++~~~~")
    print("")
    print("Day: ", day)
    print("Money: ", money)
    print("[MENTAL HEALTH]-> ", mp)
    print("Drinks Drinkn': ", drinks)
    print("")
    print("[ ] [ ] [ ] [ ] [ ] [ ]")
    print("        Juices")
    print(juices)
    print("Money A Day: ", mpd)
    print("Money made Yesterday: ", mmy)
    print("[ ] [ ] [ ] [ ] [ ] [ ]")
    print("")
    print("==========Actions==========")
    print("Sell | Skip | Drink | Quit | Fund | Acheivements (ACH)")
    action = str(input("Make an Action: "))
    clear()

    if action == "Drink" or action == "drink":
        if mp < 100:
            mp += 10
            mpchange = 10
            if mp > 100:
                mp = 100
        if mp == 100:
            moneyextra += 2
            mpchange = 0
        else: 
            mp += 20
            mpchange = 20
        print("You had a nice bottle of juice.")
        if mpchange == 0:
            print("You feel extra lucky today.")
            print("")
        drinks += 1
        day += 1
        daysober = 0
        drinkstreak +=1
#actions and stuff
    skip()
    sell()
    
    if action == 'quit' or action == 'Quit':
        quit()
        
    #funding stuff action or something
    if action == 'fund' or action == 'Fund':
        fund()
    #acheivements
    if action == 'ACH' or action == 'acheivements' or action == "ach" or action == "Acheivements":
        #print acheivements (handler is at bottom.)
        acheivements()
    
    if preday != day:
        goodday = random.randint(1,25)
        superday = random.randint(1,100)
        badday = random.randint(1,25)
        sillystuff = random.randint(1,100)
        if superday == superlucky:
            moneyextra += 3
        if goodday == luck:
            moneyextra += 1
        if badday == luck:
            badmoney += 1
            badstuff = random.randint(1,10)
        mmy = ((mpd*moneyextra)/badmoney)*brewmultiplier[brewlevel]
        money += mmy
        fruit = 0
        if action != "drink" or action != "Drink":
            drinkstreak = 0
            daysober += 1
        juicecheck = random.randint(1,25)
        superjuicecheck = random.randint(1,100)
        sfruit = 0
        if superjuicecheck == superlucky:
            fruit = superfruits[random.randint(0,7)]
            sfruit = 1
        elif juicecheck == luck:
            fruit = fruits[random.randint(0,7)]
        if fruit != 0:
            print("Your juice maker made a new juice!")
            juices.append(f"{fruit} Juice")
            print(f"They made {fruit} Juice!")
            if sfruit == 1:
                juicecosts.append(random.randint(10,money)*moneyextra)
            else:
                juicecosts.append(random.randint(1,(money/money))*moneyextra)
            s(2)
        #events
            if sillystuff == 10:
                print("Investors like your brewery. You made 2000 dollars!")
                money += 2000
            if sillystuff == 20:
                print("Investors sold their stocks in your company. Lose 100 Dollars.")
                money -= 100
        #end of events
        print("The day has ended!")
        s(2)
        clear()
        if money < 0:
            money = 0
        mp -= (random.randint(1,10)+badstuff)
        #ranks
        if money > 1000000000:
            rank = "Bud Light if they was Good"
        elif money > 1000000:
            rank = "Good Drinks made here"
        elif money > 10000:
            rank = "The Juice Man"
        elif money > 1000:
            rank = "Decent Drinks"
        elif money > 100:
            rank = "Small Startup"
        elif money > 10:
            rank = "Just a Side Project"
        elif money < 10:
            rank = "Hobby Obsessed Chuderooney"
        if money == 0:
            rank = "It's Not Working for you. Tried Gambling?"

    #ACHEIVEMENT HANDLER
    if money >= 1000000:
        bigboss = 1
    if drinks >= 100:
        alcoholism = 1
        juices.append("Barley Juice With Hops")
        juicecosts.append((money*money)*brewmultiplier[brewlevel])
    for x in juices:
        if x  == "67 Mango Juice":
            unfunny = 1
    if juicecount >= 10:
        connoisseur = 1
    if money == 0:
         broke = 1
     #end of acheivement handler
         #end of game
        