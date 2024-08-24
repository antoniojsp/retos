import random
import tkinter as tk
from tkinter import messagebox

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
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")

        self.deck = Deck()
        self.player = Player(name="Player")
        self.dealer = Player(name="Dealer", balance=float('inf'))
        self.pot = 0

        self.setup_ui()

    def setup_ui(self):
        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.player.balance}")
        self.balance_label.pack()

        self.bet_label = tk.Label(self.root, text="Enter your bet: ")
        self.bet_label.pack()

        self.bet_entry = tk.Entry(self.root)
        self.bet_entry.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.place_bet)
        self.deal_button.pack()

        self.player_hand_label = tk.Label(self.root, text="Player's hand: ")
        self.player_hand_label.pack()

        self.dealer_hand_label = tk.Label(self.root, text="Dealer's hand: ")
        self.dealer_hand_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit, state=tk.DISABLED)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand", command=self.player_stand, state=tk.DISABLED)
        self.stand_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def place_bet(self):
        try:
            bet = float(self.bet_entry.get())
            if 0 < bet <= self.player.balance:
                self.pot += bet * 2
                self.player.balance -= bet
                self.update_balance_label()
                self.deal_initial_cards()
                self.hit_button.config(state=tk.NORMAL)
                self.stand_button.config(state=tk.NORMAL)
                self.deal_button.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error", "Invalid bet amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input, please enter a number.")

    def deal_initial_cards(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck = Deck()

        self.player.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())

        self.update_hand_labels()

    def player_hit(self):
        self.player.add_card(self.deck.draw_card())
        self.update_hand_labels()
        if self.player.hand_value() > 21:
            self.end_round("You busted! Dealer wins.")

    def player_stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.dealer_turn()
        self.resolve_game()

    def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            self.dealer.add_card(self.deck.draw_card())
        self.update_hand_labels()

    def resolve_game(self):
        player_value = self.player.hand_value()
        dealer_value = self.dealer.hand_value()

        if dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            self.end_round("You win!")
            self.player.balance += self.pot
        elif player_value > 21 or dealer_value > player_value:
            self.end_round("Dealer wins.")
        else:
            self.end_round("It's a tie!")
            self.player.balance += self.pot / 2

    def end_round(self, message):
        self.result_label.config(text=message)
        self.update_balance_label()
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.deal_button.config(state=tk.NORMAL)

    def update_hand_labels(self):
        self.player_hand_label.config(text=f"Player's hand: {self.player.hand} (Value: {self.player.hand_value()})")
        self.dealer_hand_label.config(text=f"Dealer's hand: {self.dealer.hand} (Value: {self.dealer.hand_value()})")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.player.balance}")


def main():
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()