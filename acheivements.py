from termcolor import colored as c
#variables
bigboss = 0
alcoholism = 0
unfunny = 0
connoisseur = 0
broke = 0
sober = 0
daysober = 0
drinkstreak = 0

def acheivements():
    #when you want a new acheivement, add it to the bottom of game.py
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
    if sober == 1:
        print(c("Sober: Never Drink for 100 days.", 'green'))
    else:
        print(c("Sober: Never Drink for 100 days.", 'red'))
    print("")
    input("Press Enter to Continue")

def ach_handler():
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
    if drinkstreak == 0 and daysober >= 100:
        sober = 1