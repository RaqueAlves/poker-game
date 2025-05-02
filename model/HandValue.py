from itertools import combinations

class HandValue:
    def __init__(self, hand_cards, community_cards):
        self.cards = hand_cards + community_cards  # 7 cartas no total

    def calcular_forca(self):
        melhores_maos = combinations(self.cards, 5)
        
        melhor_mao = max(melhores_maos, key=self._avaliar_mao)

        return melhor_mao

    def _avaliar_mao(self, mao):
        return sum(self._valor_carta(c) for c in mao)

    def _valor_carta(self, carta):
        valores = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return valores.get(carta.rank, 0)
