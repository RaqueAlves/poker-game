from model.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        suits = ['Copas', 'Ouros', 'Espadas', 'Paus']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            raise IndexError("Não há mais cartas no baralho.")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)