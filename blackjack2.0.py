# Let's go, Dream Team!
import random

## --------------------------------------------------------------------------##

## Classes:
    # Deck
    # Card
    # Player
    # Table

#-----------------------------------------------------------------------------#
class Card(): # 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
         return "{} of {}".format(self.value, self.suit)

    #def resize_cards(card):
        # Open the image
        #our_card_img = Image.open(card)

        # Resize The Image
        #our_card_resize_image = our_card_img.resize((150, 218))
    
        # output the card
        #global our_card_image
        #our_card_image = ImageTk.PhotoImage(our_card_resize_image)

        # Return that card
        #return our_card_image 

class Deck():
    def __init__(self):
        global cards
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

    def deal(self):
        self.hand.append(self.draw)  
        self.hand.append(self.draw)
        self.dealer_hand.append(self.draw)
        self.dealer_hand.append(self.draw)
        # Change to have only 1 card viewed

    def show(self):
        for card in self.cards:
            card.show()

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.dealer_hand = []
        self.player_spot = 0


class Table():
    def __init__(self):
        pass

    def start_game(self):
        # 1st - option to start game upon opening program
        play_game = input("Would you like to begin? [Y / N] ").capitalize()
        if play_game == "Y": 
            Deck.build_deck(self)
            self.run_game()
        
    def run_game(self):
        self.cards.shuffle_cards()
        self.deal() # dealer has two cards, player has two cards
        # option for player to hit or stand
        game = self.bust()
        if game == "BUST!": 
            return "Dealer Wins"
        elif game == "STAND":
            self.dealer_bust() # determine if the player's stand wins or the Dealer prevails

        elif game == "BLACKJACK!!!":
            return "Player Wins"
        
        
    
    def hit_me(self):
        global player_spot
        if player_spot < 5:
            player_hand = random.choice(self.cards)
            self.cards.remove(player_hand)
            self.hand.append(player_hand)
           

    def bust(self):
        player_hand = sum(self.hand)
        while self.hand:
            if player_hand > 21:
                return "BUST!"
            elif player_hand < 21:
                pass # hit or pass button
            elif player_hand == 21:
                return "BLACKJACK!!!"
        return self

    def dealer_hit(self):
        global dealer_spot
        if dealer_spot < 5:
            dealer_view = random.choice(self.cards)
            self.cards.remove(dealer_view)
            self.hand.append(dealer_view)
            

    def dealer_bust(self):
        dealer_total = sum(self.dealer_hand)
        while self.dealer_hand:
            if dealer_total > 16:
                if dealer_total > self.player_hand and dealer_total <= 21:
                    return "Dealer Wins"
                elif dealer_total <= 21 and dealer_total < self.player_hand:
                    return "Player Wins"
            elif dealer_total < 16:
                self.dealer_hit()

#def main():
    ## DRIVER CODE ##
ui = Table()
ui.start_game()

#if __name__=="__main__":
 #   main()