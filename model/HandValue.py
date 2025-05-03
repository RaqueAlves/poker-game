from itertools import combinations

class HandValue:
    def __init__(self, hand_cards, community_cards):
        self.cards = hand_cards + community_cards
        self.ranking = {
            "Royal Flush": 1,
            "Straight Flush": 2,
            "Four of a Kind": 3,
            "Full House": 4,
            "Flush": 5,
            "Straight": 6,
            "Three of a Kind": 7,
            "Two Pair": 8,
            "One Pair": 9,
            "High Card": 10
        }

    def calcular_forca(self):
        melhores_maos = combinations(self.cards, 5)

        return next(melhores_maos)

    def _avaliar_mao(self, mao):
        pass

    def _valor_carta(self, carta):
        valores = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return valores.get(carta.rank, 0)
