# Let's go, Dream Team!
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Dream Team Blackjack')
root.iconbitmap('./images/Blackjack project icon.png')
root.geometry("1200x800")
root.configure(background="green")
#--------------------START GAME CODE-----------------------------------------#
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
    
    def hit_me(self):
        self.hand.append(deck.draw())
        for card in self.hand():
            if sum(self.hand) > 21:
                return "BUST!"
            elif sum(self.hand) < 21:
                pass
            elif sum(self.hand) == 21:
                return "BLACKJACK!!!"
        return self

    def show_cards(self):
        for card in self.hand:
            card.show()

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck():
    def __init__(self):
        pass
        self.cards = []

    def build_deck(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
        for suit in suits:
            for value in range(1,14):
                self.cards.append(Card(suit, value))
        
    def shuffle_cards(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
       
    def draw(self):
        return self.cards.pop()

    def deal():
        pass
    
    def show(self):
        for card in self.cards:
            card.show()

class Player_UI():
    def __init__(self):
        pass

    def start_game(self):
        # self.cards.shuffle_cards()
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


#-----------------------------------------------------------------#
#--------------START TKINTER FOOTER CODE--------------------------#
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create a couple buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command=stand)
stand_button.grid(row=0, column=2)



# Shuffle Deck On Start, should be handled in UI now
# shuffle()


root.mainloop()


# ---------Driver Code-----------#
#if __name__ == '__main__':
#    Game.play_game() ##Need to adjust for this game.


deck = Deck()
# deck.build_deck()
deck.show()