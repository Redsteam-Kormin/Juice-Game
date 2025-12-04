#PLEASE INSTALL TERMCOLOR!
import os, sys, time, random
from os import system
from time import sleep as s
from termcolor import colored as c

def clear():
    system('clear')
def quit():
    sys.exit()

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
luck = random.randint(1,25)
superlucky = random.randint(1,100)
fruits = ["Green Apple", "Grape", "Mango", "Pineapple", "Orange", "Peach", "Lemon","Lime"]
superfruits = ["Golden Apple", "Gemmy Grape", "67 Mango", "Big Pineapple", "Tangerine", "Apricot", "Pink Lemon", "Key Lime"]

#Brewery Upgrade Variables
brewlevel = 0
fundcosts = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
brewmultiplier = [1,2,4,8,16,32,64]

#acheivements
bigboss = 0
alcoholism = 0
unfunny = 0
connoisseur = 0
broke = 0

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
            moneyextra += 1
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

    if action == "Skip" or action == 'skip':
        day +=1

    if action == "Sell" or action == 'sell':
        juicefound = 0
        print("Juices: ")
        print(juices)
        print("")
        print("What Would you like to sell?")
        print("----------------------------")
        print("Choose A Juice's Name, Must be Case-Sensitive.")
        selljuice = str(input("Juice Name: "))

        for x in juices:
            print(x)
            if selljuice == x:
                juicefound = 1
            if juicefound == 1:
                juiceindex = juices.index(x)
                y = juicecosts[juiceindex]
                juiceprice = (y*moneyextra)+random.randint(1,20)*2
                money += juiceprice
                juicecosts.remove(y)
                juices.remove(x)
                print(f"You sold that juice and made {juiceprice}")
        for x in juices:
            if x == selljuice:
                print("it didnt work.")
        day += 1
        juicecount = 0
        for x in juices:
            juicecount +=1
        if juicecount == 0:
            print("You can't make money if you have nothing to sell. You Lose!")
            quit()
            break
    if action == 'quit' or action == 'Quit':
        clear()
        print(f"You made {money} dollars! Good Work.")
        print(name)
        quit()
    #funding stuff action or something
    if action == 'fund' or action == 'Fund':
        #variables for this stuff
        fundact = 0
        #start of fund stuff
        clear()
        print("Funding Options:")
        print("------------------")
        print("1. Brewery Upgrade ")
        print("     *Make more Money*")
        print("2. Juice Research ")
        print("     *Make new Juice*")
        print("     *Costs 1000 Moneys*")
        print("------------------")
        print("(Please enter number of option)")
        fundact = int(input("What would you like to fund? "))
        if fundact == 1:
            clear()
            print("-- Brewery Upgrade --")
            print(f"Current Level: {brewlevel}")
            print(f"    Current Multiplier: {brewmultiplier[brewlevel]}")
            print(f"Next Level: {brewlevel+1}")
            print(f"    Next Multiplier: {brewmultiplier[brewlevel+1]}")
            if money >= fundcosts[brewlevel]:
                brewlevel += 1
                money -= fundcosts[brewlevel]
                print(f"Brewery is now level {brewlevel}")
                s(2)
                clear()
                day += 1
        if fundact == 2:
            print("Juice Making time!")
            if money >= 1000:
                money -= 1000
                print("Your juice maker made a new juice!")
                juices.append(f"{fruit} Juice")
                print(f"They made {fruit} Juice!")
                if sfruit == 1:
                    juicecosts.append(random.randint(10,20)*moneyextra)
                else:
                    juicecosts.append(random.randint(1,10)*moneyextra)
                s(2)
    #acheivements
    if action == 'ACH' or action == 'acheivements' or action == "ach" or action == "Acheivements":
        #print acheivements (handler is at bottom.)
        clear()
        print("++++~~~~++++~~~~++++~~~~++++ACHEIVEMENTS++++~~~~++++~~~~++++~~~~++++")
        if bigboss == 1:
            print(c("The Big Boss: Get 1000000 Moneys", 'green'))
        else:
            print(c("The Big Boss: Get 1000000 Moneys", 'red'))
        if alcoholism == 1:
            print(c("True Alcoholism: Drink 100 Drinks. (Gives a SPECIAL DRINK)", 'green'))
        else:
             print(c("True Alcoholism: Drink 100 Drinks. (Gives a SPECIAL DRINK)", 'red'))
        if unfunny == 1:
            print(c("Unfunny Jokester: Get a 67 Mango Juice", 'green'))
        else:
            print(c("Unfunny Jokester: Get a 67 Mango Juice", 'red'))
        if connoisseur == 1:
            print(c("Juice Connoisuer: Have 10 Juices", 'green'))
        else:
            print(c("Juice Connoisuer: Have 10 Juices", 'red'))
        if broke == 1:
            print(c("Broke: Get down to 0 Moneys", 'green'))
        else:
            print(c("Broke: Get down to 0 Moneys", 'red'))
        print("")
        input("Press Enter to Continue")
    
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
        money += ((mpd*moneyextra)/badmoney)*brewmultiplier[brewlevel]
        fruit = 0
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
    for x in juices:
        if x  == "67 Mango Juice":
            unfunny = 1
    if juicecount >= 10:
        connoisseur = 1
    if money == 0:
         broke = 1
     #end of acheivement handler
         #end of game
        