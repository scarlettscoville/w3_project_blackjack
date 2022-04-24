# Let's go, Dream Team!


import random
from tkinter import *

root = Tk()
root.title('Dream Team Blackjack')
root.iconbitmap('./images/Blackjack project icon.png')
root.geometry("900x500")
root.configure(background="green")
#------------Will move to Classes----------------
def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2,15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Create players
    global dealer, player
    dealer = []
    player = []

    # Grab a random card for dealer
    card = random.choice(deck)
    # Remove card from deck
    deck.remove(card)
    # Append card to dealer list
    dealer.append(card)
    # Output card to screen
    dealer_label.config(text=card)

    # Grab a random card for player
    card = random.choice(deck)
    # Remove card from deck
    deck.remove(card)
    # Append card to player list
    player.append(card)
    # Output card to screen
    player_label.config(text=card)

def hit_me():
    try:
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        dealer_label.config(text=card)

        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        player_label.config(text=card)
    
    except:

#---------------------------------------------------

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

shuffle_button = Button(root, text="Shuffle Deck", font=("Ariel", 14), command=shuffle)
shuffle_button.pack(pady=20)

hit_button = Button(root, text="Hit", font=("Ariel", 14), command=hit_me)
hit_button.pack(pady=20)





root.mainloop()
#------------------------GAME--------------------------------------#


class Dealer():
    def __init__(self):
        pass
    
    def hit_me():
        # if sum of two cards is 16 and below, hit
            # if 17 or above, pass
        pass

    def show_cards():
        pass

    def clear_screen():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        # puts cards back in deck - reinitializes deck

class Player():
    def __init__(self):
        pass
    
    def hit_me():
        #else loop back
        pass

    def show_cards():
        pass

class Deck():
    def __init__(self):
        pass

    # holds our card values
    
    def shuffle_cards():
        pass
       
        

    def deal_cards():
        pass

class Player_UI():
    def __init__(self):
        pass

    def start_game():
        # 1st - option to start game upon opening program
        # graphics menu
        pass
    
    def start_hand():
        # -bets 
        # -deal cards (both cards available to player, only one dealer card shown)
        # -shuffle
        # input - play again?
        pass
    
    def hit_me():
        # input: Do you want to hit or pass?
        # will work before the dealer.hit_me
        pass

    # Driver Code #
#if __name__ == '__main__':
#    Game.play_game() ##Need to adjust for this game.