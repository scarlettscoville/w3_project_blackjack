## Classes:
    # Deck
    # Card
    # Player
    # Table
    
# Tasks
    # Logic who states who wins
        # If-Else for bust logic
    # Finishing out which cards indicate which values (K,Q,J,A)
    # Hit Me Function
        # Stand function
    # Dealer hits if value below 16
    # Running Score
    # Dealer Hand
    # Create a method if the player got Blackjack on the first round (if val == 21 return BlackJack)
    # 
import random

class Deck():
    global cards
    cards = []

    def __init__(self):
        self.build_deck()
        
    def build_deck(self):
        for suits in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1,14):
                cards.append(Card(suits,value))

    def shuffle_deck(self):
        for i in range(len(cards) -1, 0, -1):
            r = random.randint(0, i)
            cards[i], cards[r] = cards[r], cards[i]

    def draw_card(self):
        return cards.pop()

    def show(self):
        for card in cards:
            card.show()

class Card(Deck):

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print(f'{self.val} of {self.suit}')

class Player(Deck):

    def __init__(self, name, dealer=False):
        self.name = name
        self.hand = []
        self.dealer = dealer
        self.value = 0
        
    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def deal_card(self):
        hand = []
        for card in range(1):
            self.draw_card(deck)
        return hand

    def dealer_display(self):
        if self.dealer:
            print("Hidden")
            print(self.hand[1])

    def show_hand(self):
        for card in self.hand:
            card.show()

    # Need to test
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.hand:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

class Table_UI(Deck):
    def __init__(self, player):
        self.player = player

    def play_game(self):
        user_opt = input("Welcome to DT Blackjack. Would you like to play? [Y/N] ").capitalize()
        if user_opt == "Y":
            player_hand = self.player.deal_card()
            self.player.show_hand()
            dealer_hand = self.player.deal_card()
            


            

            

        





deck = Deck()
deck.shuffle_deck()

deck = Deck()
deck.shuffle_deck()

dak = Player("Dak")
dak.deal_card()

test = Table_UI(dak)
test.play_game()
# dak.show_hand()
# dak.show_dealer()