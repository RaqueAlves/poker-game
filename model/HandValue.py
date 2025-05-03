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
        melhor_info = None

        for mao in melhores_maos:
            nome, rank_numerico, carta_alta = self._avaliar_mao(mao)
            if not melhor_info or rank_numerico < melhor_info[1] or (
                rank_numerico == melhor_info[1] and carta_alta > melhor_info[2]
            ):
                melhor_info = (nome, rank_numerico, carta_alta)

        return melhor_info  # Ex: ("Flush", 5, 13)

    def _avaliar_mao(self, mao):
        valores = sorted([self._valor_carta(carta) for carta in mao], reverse=True)
        naipes = [carta.suit for carta in mao]
        contagem_valores = Counter(valores)
        contagem_naipes = Counter(naipes)

        eh_flush = max(contagem_naipes.values()) == 5
        eh_straight = self._verifica_straight(valores)

        if eh_flush and eh_straight:
            if valores[0] == 14 and valores[1] == 13:
                return ("Royal Flush", self.ranking["Royal Flush"], 14)
            return ("Straight Flush", self.ranking["Straight Flush"], valores[0])
        if 4 in contagem_valores.values():
            quadra = [v for v, c in contagem_valores.items() if c == 4][0]
            return ("Four of a Kind", self.ranking["Four of a Kind"], quadra)
        if 3 in contagem_valores.values() and 2 in contagem_valores.values():
            trio = [v for v, c in contagem_valores.items() if c == 3][0]
            return ("Full House", self.ranking["Full House"], trio)
        if eh_flush:
            return ("Flush", self.ranking["Flush"], valores[0])
        if eh_straight:
            return ("Straight", self.ranking["Straight"], valores[0])
        if 3 in contagem_valores.values():
            trio = [v for v, c in contagem_valores.items() if c == 3][0]
            return ("Three of a Kind", self.ranking["Three of a Kind"], trio)
        if list(contagem_valores.values()).count(2) == 2:
            pares = sorted([v for v, c in contagem_valores.items() if c == 2], reverse=True)
            return ("Two Pair", self.ranking["Two Pair"], pares[0])
        if 2 in contagem_valores.values():
            par = [v for v, c in contagem_valores.items() if c == 2][0]
            return ("One Pair", self.ranking["One Pair"], par)
        return ("High Card", self.ranking["High Card"], valores[0])

    def _verifica_straight(self, valores):
        valores = list(sorted(set(valores), reverse=True))
        if len(valores) < 5:
            return False
        for i in range(len(valores) - 4):
            if valores[i] - valores[i + 4] == 4:
                return True
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