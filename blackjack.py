# Let's go, Dream Team!


from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text = "Dream Team Blackjack")
myLabel2 = Label(root, text = "built by Scarlett, Dak, and Grady")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

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
        # Look into Fisher-Yates shuffle for shuffling algorithm? [https://www.youtube.com/watch?v=4zx5bM2OcvA]

    def deal_cards():
        pass

class Player_UI():
    def __init__(self):
        pass

    def start_game():
        # 1st - option to start game upon opening program
        play_game = input("Would you like to begin? [Y / N] ").capitalize()
        if play_game == "Y":
            
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