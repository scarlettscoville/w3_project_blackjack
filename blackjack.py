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
player_frame.grid(row=1, column=0, ipadx=20, pady=20,)

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

shuffle_button = Button(root, text="Shuffle Deck", font=("Ariel", 14))
shuffle_button.pack(pady=20)

hit_button = Button(root, text="Hit", font=("Ariel", 14), command=hit_me)
hit_button.pack(pady=20)


root.mainloop()
#------------------------GAME--------------------------------------#


class Dealer():
    def __init__(self):
        pass
    
    def hit_me():
        global dealer_spot
        if dealer_spot < 5:
            try:
                dealer_card = random.choice(deck)
                deck.remove(dealer_card)
                dealer.append(dealer_card)
                global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
                
                if dealer_spot == 0:
                    # Resize Card
                    dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
                    # Output card to screen    
                    dealer_label_1.config(image=dealer_image)
                    # Increment dealer card by 1
                    dealer_spot += 1
                elif dealer_spot == 1:
                    # Resize Card
                    dealer_image1 = resize_cards(f'images/cards/{dealer_card}.png')
                    # Output dealer_card to screen    
                    dealer_label_1.config(image=dealer_image1)
                    # Increment dealer card by 1
                    dealer_spot += 1
                elif dealer_spot == 2:
                    # Resize Card
                    dealer_image2 = resize_cards(f'images/cards/{dealer_card}.png')
                    # Output card to screen    
                    dealer_label_2.config(image=dealer_image2)
                    # Increment dealer card by 1
                    dealer_spot += 1
                elif dealer_spot == 3:
                    # Resize Card
                    dealer_image3 = resize_cards(f'images/cards/{dealer_card}.png')
                    # Output card to screen    
                    dealer_label_3.config(image=dealer_image3)
                    # Increment dealer card by 1
                    dealer_spot += 1
                elif dealer_spot == 4:
                    # Resize Card
                    dealer_image4 = resize_cards(f'images/cards/{dealer_card}.png')
                    # Output card to screen    
                    dealer_label_4.config(image=dealer_image4)
                    # Increment dealer card by 1
                    dealer_spot += 1

                root.title(f'Dream Team Blackjack - {len(deck)} Cards Left')



            except:
                root.title(f'Dream Team Blackjack')

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
        # Shuffle 2 cards for player and dealer
        
       

    def deal_cards():
        pass

class Player_UI():
    def __init__(self):
        pass

    def start_game():
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

    # Driver Code #
#if __name__ == '__main__':
#    Game.play_game() ##Need to adjust for this game.