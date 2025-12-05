import os, sys, time, random
from os import system
from time import sleep as s
#clear, but easier to write.
def clear():
    system('clear')
#quit, but easier to write.  
def quit():
    clear()
    print(f"You made {money} dollars! Good Work.")
    print(name)
    sys.exit()
#skip action  
def skip():
  if action == "Skip" or action == 'skip':
    day +=1
    clear()
    print("You skipped a day.")
    s(1)

#sell action
def sell():
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
#fund action
def fund():
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