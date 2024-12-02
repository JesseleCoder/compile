import random
import tkinter as tk
from tkinter import messagebox

Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Deck = Cards * 4
random.shuffle(Deck)
Dealer = []
Player = []
toprint = []

def deal(Deck):
    for i in range(2):
        Dealer.append(Deck.pop())
        Player.append(Deck.pop())
    return Dealer, Player

# Adjust the Getcardvalue function to handle Ace doing stuff, starting as 11 or 1 based on total

def Getcardvalue(card, current_total=0):
    if card == 11 or card == 12 or card == 13:
        return 10
    elif card == 14:
        if current_total + 11 > 21:
            return 1
        else:
            return 11
    else:
        return card


def Getcardname(card):
    if card == 11:
        return "Jack"

    elif card == 12:
        return "Queen"

    elif card == 13:
        return "King"

    elif card == 14:
        return "Ace"

    else:
        return str(card)


# Modify Total to consider the Ace special behavior

def Total(Hand):
    total = 0
    aces_count = 0
    for card in Hand:
        if card == 14:
            aces_count += 1
        total += Getcardvalue(card, total)
    while total > 21 and aces_count > 0:
        total -= 10  # Adjust for Ace being 1 instead of 11
        aces_count -= 1
    return total


def PrintHand(Hand):
    toprint.clear()  # Clear previous hand names
    for card in Hand:
        toprint.append(Getcardname(card))

    return toprint  # Return the list of card names


def Hit(Hand):
    Hand.append(Deck.pop())
    return Hand


def Check(Hand):
    if Total(Hand) == 21:
        return True
    else:
        return False


def printgame(Dealer, Player):
    # print(f"Dealer's Hand: {PrintHand(Dealer)}")
    print(f"Player's Hand: {PrintHand(Player)}")


def DealerTurn(Dealer):
    while Total(Dealer) < 17: #random.randint(5, 19):
        Hit(Dealer)
        printgame(Dealer, Player)
        if Total(Dealer) > 21:  # Check if dealer busts
            print("Dealer Bust!")
            break


def plrturn(Player):
    while True:
        choice = input("Hit or Stand? ")
        if choice.lower() == "hit":
            Hit(Player)
            printgame(Dealer, Player)
            if Total(Player) > 21:
                print("Bust! Dealer wins!")
                break

        elif choice.lower() == "stand":
            print("Player stands.")
          
            DealerTurn(Dealer)
            print(f"Dealer's Hand: {PrintHand(Dealer)}")
            print(f"Player's Hand: {PrintHand(Player)}")
            if Total(Dealer) > 21:
                print("Dealer busts! Player wins!")
            elif Total(Dealer) > Total(Player):
                print("Dealer wins!")
            elif Total(Dealer) < Total(Player):
                print("Player wins!")
            else:
                print("MESSAGE.GAME_END")
            break  # End loop after player stands
        else:
            print("Invalid input")
deal(Deck)
printgame(Dealer, Player)
plrturn(Player)
