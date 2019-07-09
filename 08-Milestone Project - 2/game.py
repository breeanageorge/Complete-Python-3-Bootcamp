"""
Blackjack Game
"""
import random
#Variables
suites = ['Hearts','Diamonds','Spades','Clubs']
card_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
deck = []
num_cards = 51
start_amount = 100
dealer_check = 0
player_check = 0

#Object Classes
class Card():
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suite}"

class Player():
    def __init__(self, bank=100, cards=[]):
        self.bank = bank
        self.cards = cards

    def bet(self, amount=0):
        self.bank -= amount

    def win(self, amount=0):
        self.bank += amount
        print(f'You win! Bank balance is now ${self.bank}')

    def printCards(self):
        for x in self.cards:
            print(x)

class Dealer():
    def __init__(self, cards=[]):
        self.cards = cards

    def printCards(self):
        for x in self.cards:
            print(x)

#Functions
def dealCard(person, num_card):
    temp_card = random.randint(0, num_card)
    person.cards.append(deck[temp_card])
    del deck[temp_card]
    num_card -= 1
    return num_card

def checkWin(person):
    total = 0
    aces = 0
    for x in person.cards:
        total += card_values[x.value]
        if x.value == 'Ace':
            aces += 1

    if aces > 0:
        for a in range(1,aces):
            if total > 21:
                total -= 10

    if total < 21:
        return total
    elif total == 21:
        return True
    else:
        return False

def blackJack(start_amount):
    #Create Deck
    for s in suites:
        for c in card_values.keys():
            deck.append(Card(s,c))

    #Initiate dealer and player
    dealer = Dealer()
    player = Player(start_amount)

    #Player bet
    while True:
        try:
            player_bet = int(input("What is your initial bet?"))
        except:
            print("Please input a number.")
            continue
        else:
            if player.bank >= player_bet:
                player.bet(player_bet)
                print(f'${player_bet} bet placed, ${player.bank} left!')
                break
            else:
                print(f'Funds unavailible, ${player.bank} left')
                continue

    #First round
    num_cards = dealCard(dealer, num_cards)
    num_cards = dealCard(dealer, num_cards)
    print(f"Dealer's starting hand is HIDDEN and {dealer.cards[1]}")

    num_cards = dealCard(player, num_cards)
    num_cards = dealCard(player, num_cards)
    print(f"Your starting hand is {player.cards[0]} and {player.cards[1]}")

    dealer_check = checkWin(dealer)
    player_check = checkWin(player)

    #Player Turn
    while type(player_check) == int:
        #Check hit or stay

        #If hit dealCard and checkWin, else break


    #Dealer Turn
    while type(dealer_check) == int and type(player_check) == int:
        asdf


    if player_check == True:
        print(f"You got 21, you win!")
    elif player_check == False:
        print(f"You busted, dealer wins!")
    elif dealer_check == True:
        print(f"Dealer got 21, dealer wins!")
    elif player_check == False:
        print(f"Dealer busted, you win!")
    elif player_check > dealer_check:
        print(f"You win! Your total {player_check}, dealer total {dealer_check}")
    else:
        print(f"Dealer wins! Your total {player_check}, dealer total {dealer_check}")

    while True:
        play_again = input("Do you want to play again? Y or N")
        if play_again == 'Y' or play_again =='y':
            blackJack(player.bank)
            break
        elif play_again == 'N' or play_again =='n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid input")
