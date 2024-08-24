# app/models.py
import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11  # Ace can be 1 or 11, we'll handle that later
}


class Deck:
    def __init__(self):
        self.cards = [rank for rank in card_values.keys() for _ in range(4)]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.hand = []

    def hand_value(self):
        value = sum(card_values[card] for card in self.hand)
        ace_count = self.hand.count('A')
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(name="Player")
        self.dealer = Player(name="Dealer", balance=float('inf'))
        self.pot = 0

    def start_new_round(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck = Deck()

        self.player.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())

    def player_hit(self):
        self.player.add_card(self.deck.draw_card())
        if self.player.hand_value() > 21:
            return "bust"
        return "continue"

    def player_stand(self):
        while self.dealer.hand_value() < 17:
            self.dealer.add_card(self.deck.draw_card())
        return self.resolve_game()

    def resolve_game(self):
        player_value = self.player.hand_value()
        dealer_value = self.dealer.hand_value()

        if dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            return "win"
        elif player_value > 21 or dealer_value > player_value:
            return "lose"
        else:
            return "tie"