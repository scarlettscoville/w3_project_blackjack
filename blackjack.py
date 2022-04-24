# Let's go, Dream Team!


import random
from tkinter import *

root = Tk()
root.title('Dream Team Blackjack')
root.iconbitmap('./images/Blackjack project icon.png')
root.geometry("900x500")
root.configure(background="green")


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

shuffle_button = Button(root, text="Shuffle Deck", font=("Ariel", 14))
shuffle_button.pack(pady=20)

hit_button = Button(root, text="Hit", font=("Ariel", 14))
hit_button.pack(pady=20)


root.mainloop()
#------------------------GAME--------------------------------------#


class Dealer():
    def __init__(self):
        pass
    
    def hit_me(self):
        # if sum of two cards is 16 and below, hit
            # if 17 or above, pass
        pass

    def show_cards(self):
        pass

    def clear_screen(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        # puts cards back in deck - reinitializes deck

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        pass
    
    def hit_me(self, deck):
        self.hand.append(deck.draw_cards())
        self.hand.append(deck.draw_cards())
        #else loop back
        pass

    def show_cards(self):
        for card in self.hand:
            card.show()
        pass

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} {}".format(self.suit, self.value))

class Deck(): #card class in video
    def __init__(self):
        pass

    def shuffle_cards():
        pass
       
    def draw_cards(self):
        pass

    def deal_cards():
        pass
    
    def show(self):
        print("{} of {}").format(self.value, self.suit)

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