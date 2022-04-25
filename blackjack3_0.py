## Classes:
    # Card
    # Deck
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

import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):     # Able to customize the string representation of the object. By default the output contains the memory address and the __repr__ addresses this issue
         return f'{self.value} {self.suit}'

class Deck:

    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["♠️", "♣", "♥", "♦"] for value in
                    ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        
    def shuffle_deck(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Player:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)

    def rank_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -=10

    def get_value(self):
        self.rank_value()
        return self.value

    def display(self):
        if self.dealer:
            print("Hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print('┌───────┐')
                print('| Dream |')
                print('|       |')
                print(f'|  {card}  |')
                print('|       |')
                print('| Team  |')
                print('└───────┘') 
        print("Total Card Value: ->", [self.get_value()])

class Table():
    def __init__(self):
        pass

    def play_game(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle_deck()

            self.player_hand = Player()
            self.dealer_hand = Player(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal_card())
                self.dealer_hand.add_card(self.deck.deal_card())

            print("Here is what you have: ")
            self.player_hand.display()
            print()
            print("♠️", "♣", "♥", "♦","♠️", "♣", "♥", "♦","♠️", "♣", "♥", "♦")
            print("----------$$-----------")
            print("♠️", "♣", "♥", "♦","♠️", "♣", "♥", "♦","♠️", "♣", "♥", "♦")
            print()
            print("Here is the Dealer's Hand: ")
            self.dealer_hand.display()
            print()

            game_over = False

            while not game_over:
                player_blackjack, dealer_blackjack = self.check_for_blackjack()
                if player_blackjack or dealer_blackjack:
                    game_over = True
                    self.show_blackjack(player_blackjack, dealer_blackjack)
                    continue

                choose_wisely = input("What would you like to do?  [Hit (H) or Stand (S)]? ").capitalize()
                while choose_wisely not in ["H", "S"]:
                    choose_wisely = input("What would you like to do?  [Hit (H) or Stand (S)]? ").capitalize()
                if choose_wisely == "H":
                    self.player_hand.add_card(self.deck.deal_card())
                    self.player_hand.display()
                    if self.player_hand_over():
                        print("You're bad at this! You lost! 🤣🤣🤣")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results")
                    print("Your hand ", player_hand_value)
                    print("Dealer hand ", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("Looks like you chose wisely, you won! 🙌")
                    elif player_hand_value == dealer_hand_value:
                        print("Blackjack push! It's a tie 🫠")
                    else:
                        print("Wow you're bad at this.. Dealer Won! 💸💸💸 ")

                    game_over = True

            play_again = input("Would you like to lose some money? [Y / N] ").capitalize()
            while play_again.capitalize() not in ["Y", "N"]:
                play_again = input("Would you like to lose some money? [Y / N] ").capitalize()
            if play_again.capitalize() == "N":
                print("Thanks for playing! 🤑🤑🤑")
                playing = False
            else:
                game_over = False
    
    def player_hand_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("It looks like a draw partner! 🤠🤠🤠 ")
        elif player_has_blackjack:
            print("You have Blackjack, You Win!")
        elif dealer_has_blackjack:
            print("Dealer has Blackjack, Dealer Wins! 💸💸💸")

if __name__ == "__main__":
    test = Table()
    test.play_game()
       