import random

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

cards = [
    "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
    "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
    "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
    "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"
]
hitnumber = 0
hitcards = []
botcards = []

clear()

def setup():
    card1 = random.choice(cards)
    rank = card1[:-1]
    if rank in ["10", "J", "Q", "K"]:
        value1 = 10
    elif rank == "A":
        value1 = 1
    else:
        value1 = int(rank)
    cards.remove(card1)

    card2 = random.choice(cards)
    rank = card2[:-1]
    if rank in ["10", "J", "Q", "K"]:
        value2 = 10
    elif rank == "A":
        value2 = 1
    else:
        value2 = int(rank)
    cards.remove(card2)
    return card1, value1, card2, value2

def botsetup():
    botcard1 = random.choice(cards)
    rank = botcard1[:-1]
    if rank in ["10", "J", "Q", "K"]:
        botvalue1 = 10
    elif rank == "A":
        botvalue1 = 1
    else:
        botvalue1 = int(rank)
    cards.remove(botcard1)

    botcard2 = random.choice(cards)
    rank = botcard2[:-1]
    if rank in ["10", "J", "Q", "K"]:
        botvalue2 = 10
    elif rank == "A":
        botvalue2 = 1
    else:
        botvalue2 = int(rank)
    cards.remove(botcard2)
    return botcard1, botvalue1, botcard2, botvalue2

def election():
    print("Press H to hit")
    print("Press S to Stay")
    choice = input()
    if choice in ["H","h","hit","Hit","HIT"]:
        next = True
    elif choice in ["S","s","Stay","stay","STAY"]:
        next = False
    else:
        print("Error, try again.")
        election()
    clear()
    return next

def hit():
    hitcard = random.choice(cards)
    rank = hitcard[:-1]
    if rank in ["10", "J", "Q", "K"]:
        valuehit = 10
    elif rank == "A":
        valuehit = 1
    else:
        valuehit = int(rank)
    cards.remove(hitcard)
    return hitcard, valuehit

def bothit():
    bothitcard = random.choice(cards)
    rank = bothitcard[:-1]
    if rank in ["10", "J", "Q", "K"]:
        botvaluehit = 10
    elif rank == "A":
        botvaluehit = 1
    else:
        botvaluehit = int(rank)
    cards.remove(bothitcard)
    return bothitcard, botvaluehit

#Game

card1, value1, card2, value2 = setup()      #Player setup
hitcards.append(card1)
hitcards.append(card2)
print("Your cards:")
print (hitcards)
totalvalue = value1 + value2


botcard1, botvalue1, botcard2, botvalue2 = botsetup()       #Bot setup
botcards.append(botcard1)
botcards.append(botcard2)
print("Dealers cards:")
print(botcards)
bottotalvalue = botvalue1 + botvalue2

if totalvalue > bottotalvalue:
    win = True

while election() == True:
    hitcard, hitvalue = hit()               #Player Hit
    hitcards.append(hitcard)
    print ("Your Cards:", hitcards)
    totalvalue = totalvalue + hitvalue

    if bottotalvalue < 16:                  #Bot Hit
        bothitcard, bothitvalue = bothit()
        botcards.append(bothitcard)
        print ("Dealer Cards:",botcards)
        bottotalvalue = bottotalvalue + bothitvalue

    if totalvalue > 21:
        print("You went over 21!")
        win = False
        break
    if bottotalvalue > 21:
        print("Dealer went over 21!")
        win = True
        break
if totalvalue > 21:
    while bottotalvalue < 17:
            nothing = input("Dealer hits, press enter to reveal")
            bothitcard, bothitvalue = bothit()
            botcards.append(bothitcard)
            print ("Dealer Cards:",botcards)
            bottotalvalue = bottotalvalue + bothitvalue

    if totalvalue > bottotalvalue:
        win = True
    elif bottotalvalue > totalvalue:
        win = False

clear()
print ("Your Cards:", hitcards)
print ("Dealer Cards:",botcards)
if win == True:
    print("You win!")
elif win == False:
    print("You lose!")

#game not finished, test change
