from itertools import combinations
from collections import Counter

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
        melhores_maos = [list(comb) for comb in combinations(self.cards, 5)]
        melhor_mao = None
        melhor_rank = float("inf")

        for mao in melhores_maos:
            rank = self._avaliar_mao(mao)
            if self.ranking[rank] < melhor_rank:
                melhor_rank = self.ranking[rank]
                melhor_mao = mao

        print(f"Melhor mão: {melhor_mao} ({self._avaliar_mao(melhor_mao)})")
        return melhor_mao

    def _avaliar_mao(self, mao):
        valores = sorted([self._valor_carta(carta) for carta in mao], reverse=True)
        naipes = [carta.suit for carta in mao]
        contagem_valores = Counter(valores)
        contagem_naipes = Counter(naipes)

        eh_flush = max(contagem_naipes.values()) == 5
        eh_straight = self._verifica_straight(valores)

        if eh_flush and eh_straight:
            if valores[0] == 14 and valores[1] == 13:
                return "Royal Flush"
            return "Straight Flush"
        if 4 in contagem_valores.values():
            return "Four of a Kind"
        if 3 in contagem_valores.values() and 2 in contagem_valores.values():
            return "Full House"
        if eh_flush:
            return "Flush"
        if eh_straight:
            return "Straight"
        if 3 in contagem_valores.values():
            return "Three of a Kind"
        if list(contagem_valores.values()).count(2) == 2:
            return "Two Pair"
        if 2 in contagem_valores.values():
            return "One Pair"
        return "High Card"

    def _verifica_straight(self, valores):
        valores = list(sorted(set(valores), reverse=True))
        if len(valores) < 5:
            return False
        for i in range(len(valores) - 4):
            if valores[i] - valores[i + 4] == 4:
                return True
        # Checa caso especial A-2-3-4-5
        if set([14, 2, 3, 4, 5]).issubset(set(valores)):
            return True
        return False

    def _valor_carta(self, carta):
        valores = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        return valores.get(carta.rank, 0)

