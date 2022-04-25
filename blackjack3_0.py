## Classes:
    # Deck
    # Card
    # Player
    # Table

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

    def __init__(self, name):
        self.name = name
        self.hand = []
        

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def deal_card(self):
        hand = []
        for card in range(1):
            self.draw_card(deck)
        return hand

    def show_hand(self):
        for card in self.hand:
            card.show()

class Table_UI(Deck):
    def __init__(self, player):
        self.player = player

    def play_game(self):
        user_opt = input("Welcome to DT Blackjack. Would you like to play? [Y/N] ").capitalize()
        if user_opt == "Y":
            player_hand = self.player.deal_card()
            self.player.show_hand()

            

            

        





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