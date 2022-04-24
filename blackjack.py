# Let's go, Dream Team!
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Dream Team Blackjack')
root.iconbitmap('./images/dtbj_favicon.png')
root.geometry("1200x800")
root.configure(background="#274e13")
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
        player_hand = sum(self.hand)
        while self.hand:
            if player_hand > 21:
                return "BUST!"
            elif player_hand < 21:
                pass
            elif player_hand == 21:
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

    # Resize Cards
    def resize_cards(card):
	    # Open the image
	    our_card_img = Image.open(card)

	    # Resize The Image
	    our_card_resize_image = our_card_img.resize((150, 218))
	
	    # output the card
	    global our_card_image
	    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	    # Return that card
	    return our_card_image    

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

    def start_game(self):
        self.players = []
        self.dealers = []

       

class Player_UI():
    def __init__(self):
        pass

    def start_game(self):
        # self.cards.shuffle_cards()
        # 1st - option to start game upon opening program
        play_game = input("Would you like to begin? [Y / N] ").capitalize()
        if play_game == "Y":
            Player_UI.start_game() # Recurrsive call
        # graphics menu
        
    
    def start_hand():
        # -bets 
        # -deal cards (both cards available to player, only one dealer card shown)
        # -shuffle
        # input - play again?
        pass
    
    def hit_me():
        global player_spot
        if player_spot < 5:
            try:
                player_card = random.choice(deck)
                deck.remove(player_card)
                player.append(player_card)
                global player_image1, player_image2, player_image3, player_image4, player_image5
                
                if player_spot == 0:
                    # Resize Card
                    player_image = resize_cards(f'images/cards/{player_card}.png')
                    # Output card to screen    
                    player_label_1.config(image=player_image)
                    # Increment player card by 1
                    player_spot += 1
                elif player_spot == 1:
                    # Resize Card
                    player_image1 = resize_cards(f'images/cards/{player_card}.png')
                    # Output card to screen    
                    player_label_1.config(image=player_image1)
                    # Increment player card by 1
                    player_spot += 1
                elif player_spot == 2:
                    # Resize Card
                    player_image2 = resize_cards(f'images/cards/{player_card}.png')
                    # Output card to screen    
                    player_label_2.config(image=player_image2)
                    # Increment player card by 1
                    player_spot += 1
                elif player_spot == 3:
                    # Resize Card
                    player_image3 = resize_cards(f'images/cards/{player_card}.png')
                    # Output card to screen    
                    player_label_3.config(image=player_image3)
                    # Increment player card by 1
                    player_spot += 1
                elif player_spot == 4:
                    # Resize Card
                    player_image4 = resize_cards(f'images/cards/{player_card}.png')
                    # Output card to screen    
                    player_label_4.config(image=player_image4)
                    # Increment player card by 1
                    player_spot += 1

                root.title(f'Dream Team Blackjack - {len(deck)} Cards Left')



            except:
                root.title(f'Dream Team Blackjack')

        # input: Do you want to hit or pass?
        # will work before the dealer.hit_me
        pass


#-----------------------------------------------------------------#
#--------------START TKINTER FOOTER CODE--------------------------#
my_frame = Frame(root, bg="#274e13")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", font=("Helvetica", 14), bd=0, bg="#222222", fg="#FFFFFF")
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", font=("Helvetica", 14), bd=0, bg="#222222", fg="#FFFFFF")
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='', bg="#222222")
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='', bg="#222222")
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='', bg="#222222")
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='', bg="#222222")
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='', bg="#222222")
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='', bg="#222222")
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='', bg="#222222")
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='', bg="#222222")
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='', bg="#222222")
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='', bg="#222222")
player_label_5.grid(row=1, column=4, pady=20, padx=20)

# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create a couple buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command= Deck.shuffle_cards)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command= Player.hit_me)
card_button.grid(row=0, column=1, padx=10)

 # stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command= stand)
 # stand_button.grid(row=0, column=2)



# Shuffle Deck On Start, should be handled in UI now
# shuffle()


root.mainloop()


# ---------Driver Code-----------#
#if __name__ == '__main__':
#    Game.play_game() ##Need to adjust for this game.


deck = Deck()
# deck.build_deck()
deck.show()