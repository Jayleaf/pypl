###############################################
#                                             #
#            Python Blackjack                 #
#        Made by Jayleaf on 2/13/22           #
#                                             #
###############################################

import os
import random
from unicodedata import numeric
from cv2 import line, split

# declare the suits and values for random picking later

suits = ['♦', '♣', '♥', '♠']
cardvalues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']

# classes for each type of thing

class Card:
  def __init__(self, facevalue, suit, realvalue, ascii):
    self.facevalue = facevalue
    self.suit = suit
    self.realvalue = realvalue
    self.ascii = ascii

class Player:
    def __init__(self, cards, cardsvalue):
        self.cards = cards
        self.cardsvalue = cardsvalue

class Dealer:
    def __init__(self, cards, cardsvalue):
        self.cards = cards
        self.cardsvalue = cardsvalue


# declare the defaults for the player and dealer

player = Player([], 0)
dealer = Dealer([], 0)

def startGame():

    # assigns the player 2 cards, the dealer 1, prints the cards in console, checks for blackjack, and then presents the hit or stand choices.

    global player
    global dealer
    player = Player([], 0)
    dealer = Dealer([], 0)
    AssignCard('player', makeCard(random.choice(cardvalues), random.choice(suits), 'player'))
    AssignCard('player', makeCard(random.choice(cardvalues), random.choice(suits), 'player'))
    AssignCard('dealer', makeCard(random.choice(cardvalues), random.choice(suits), 'dealer'))
    printCards(True)
    checkGameEndingConditions(False)
    choices()

def AssignCard(assignee, card):
    if assignee == 'dealer':
        global dealer
        dlcards = dealer.cards
        dlcards.append(card)
        dealer = Dealer(dlcards, dealer.cardsvalue) # sets the dealer's cards to dlcards, which i have to make it's own variable because i cannot append directly to the variable.
        dealer = Dealer(dealer.cards, dealer.cardsvalue + int(card.realvalue)) # adds the card's value to the dealer's total card value
    elif assignee == 'player':
        global player
        plcards = player.cards
        plcards.append(card)
        player = Player(plcards, player.cardsvalue) # same thing as dealer
        player = Player(player.cards, player.cardsvalue + int(card.realvalue))
    

def makeCard(value, suit, assignee):
    cardarray = []
    for x in range(0, 7): # simple loop for the procedural generation of cards
        if x == 0:
            cardarray.append(" -------- ")
        elif x == 1:
            cardarray.append("|{csuit}       |".format(csuit = suit))
        elif x == 2:
            cardarray.append("|        |")
        elif x == 3:
            try :
                if int(value) > 9:
                    cardarray.append("|    {cvalue}  |".format(cvalue = value))
                else:
                    cardarray.append("|    {cvalue}   |".format(cvalue = value))
            except ValueError:
                cardarray.append("|    {cvalue}   |".format(cvalue = value))
            
        elif x == 4:
            cardarray.append("|        |")
        elif x == 5:
            cardarray.append("|       {csuit}|".format(csuit = suit))
        elif x == 6:
            cardarray.append(' -------- ')

    cardascii = '\n'.join(cardarray)
    if value == 'K' or value == 'Q' or value == 'J': #
        realvalue = 10                               #
    elif value == 'A':                               #
        if assignee == 'player':                     #
            global player                            #
            if player.cardsvalue > 10:               #
                realvalue = 1                        #
            else:                                    # Logic for determining the value of faced cards. King, Queen, and Jack are 10, while the ace is 1 or 11
                realvalue = 11                       # depending on the player's total deck value.
        if assignee == 'dealer':                     #
            global dealer                            #
            if dealer.cardsvalue > 10:               #
                realvalue = 1                        #
            else:                                    #
                realvalue = 10                       #
    else:                                            #
        realvalue = value                            #
    card = Card(value, suit, realvalue, cardascii )  # Makes a new card class, and then returns that.
    return card

def printCards(shouldclear):
    global player
    global dealer

    if shouldclear == True:
        clear = lambda: os.system('cls')
        clear()

    # print the dealer's cards. card printing is done row by row to achieve a side-by-side effect.
    dcards = dealer.cards
    dcardrow = []
    print('\n Dealer\'s Cards \n')
    for x in range(0, 7):
        linearray = []
        for y in dcards:    # This is done for each card in the dealer's deck, 7 times.
            splitascii = y.ascii.split('\n') # Splits the ASCII art of the card into 7 different lines
            linearray.append(splitascii[x]) # Appends the line that corresponds to the array index to a temporary line array.
        dcardrow.append('   '.join(linearray)) # appends the card row with each xst row from the dealer's deck
    print('\n'.join(dcardrow)) # prints the row. Keep in mind this is done 7 times, to complete the cards.

    # print the player's cards.

    pcards = player.cards
    pcardrow = []
    print('\n Player\'s Cards \n')
    for x in range(0, 7):
        linearray = []
        for y in pcards:
            splitascii = y.ascii.split('\n')
            linearray.append(splitascii[x])
        pcardrow.append('   '.join(linearray))
    print('\n'.join(pcardrow))
    print('\n ------------------- \n')
    print('Player Card Value: ' + str(player.cardsvalue))
    print('Dealer Card Value: ' + str(dealer.cardsvalue))


def deinitialize():
    global player
    global dealer
    player = Player([], 0)
    dealer = Dealer([], 0)

def replay():
    returntomenu = input('Replay? (y/n): ')
    if returntomenu.lower() == 'y':
        deinitialize()
        startGame()
    elif returntomenu.lower() == 'n':
        from index import init
        init()
        deinitialize()
    else:
        print('That is not a valid choice.')
        replay()   

def checkGameEndingConditions(shouldCheckForDealerValue):
    global player
    global dealer

    if player.cardsvalue > 21:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Bust. Dealer wins!')
        replay()
    elif player.cardsvalue == 21:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Blackjack. Player wins!')
        replay()
    elif player.cardsvalue > dealer.cardsvalue and shouldCheckForDealerValue:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Player wins!')
        replay()
    elif player.cardsvalue < dealer.cardsvalue and shouldCheckForDealerValue and dealer.cardsvalue > 21:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Bust. Player wins!')
        replay()
    elif player.cardsvalue < dealer.cardsvalue and shouldCheckForDealerValue:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Dealer wins!')
        replay()
    elif player.cardsvalue == dealer.cardsvalue and shouldCheckForDealerValue:
        clear = lambda: os.system('cls')
        clear()
        printCards(False)
        print('Push. Nobody wins!')
        replay()
    else:
        printCards(True)
        choices()
    

def choices():   
    choice = input('Hit or Stand?: ')
    global player
    global dealer
    if choice.lower() == 'hit':
        AssignCard('player', makeCard(random.choice(cardvalues), random.choice(suits), 'player'))
        checkGameEndingConditions(False)
    if choice.lower() == 'stand':
        while dealer.cardsvalue < 17:
            AssignCard('dealer', makeCard(random.choice(cardvalues), random.choice(suits), 'dealer'))
            if(dealer.cardsvalue >= 17):
                checkGameEndingConditions(True)
                break
    else:
        print('Thats not a valid choice!')
        choices()
