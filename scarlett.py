from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Dream Team Blackjack')
root.iconbitmap('./images/Blackjack project icon.png')
root.geometry("900x500")
root.configure(background="green")
#------------Will move to Classes----------------
def resize_cards(card):
    # Open the image
    our_card_img = Image.open(card)

    # Resize the image
    global our_card_resize_image
    
    our_card_resize_image = our_card_img.resize((150, 218))

    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    # Return that card
    return our_card_image

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
    global dealer_image
    dealer_image = resize_cards(f'images/deck/{card}.png')

    dealer_label.config(image=dealer_image)

    # Grab a random card for player
    card = random.choice(deck)
    # Remove card from deck
    deck.remove(card)
    # Append card to player list
    player.append(card)
    # Output card to screen
    global player_image
    player_image = resize_cards(f'images/deck/{card}.png')

    player_label.config(image=player_image)

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
        pass
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