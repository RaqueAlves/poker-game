from model.Player import Player
from model.Deck import Deck
from model.HandValue import HandValue
import random

class PokerGame:
    def __init__(self, usuario):
        self.deck = Deck()
        self.players = [
            Player(usuario),
            Player("Jogador 1"),
            Player("Jogador 2"),
            Player("Jogador 3")
        ]
        self.community_cards = []
        self.dealer_index = 0
        self.pot = 0
        self.aposta_atual = 0

    def atualizar_posicoes(self):
        self.shuffle()
        num_players = len(self.players)
        self.dealer_index = (self.dealer_index + 1) % num_players

        for player in self.players:
            player.role = "normal"
        
        self.players[self.dealer_index].role = "dealer"
        self.players[(self.dealer_index + 1) % num_players].role = "small_blind"
        self.players[(self.dealer_index + 2) % num_players].role = "big_blind"
    
    def obter_jogador_por_role(self, role):
        return next((j for j in self.players if j.role == role), None)
    
    def ordem_apostas(self):
        start_index = (self.dealer_index + 3) % len(self.players)
        return self.players[start_index:] + self.players[:start_index]

    def shuffle(self):
        random.shuffle(self.players)

    def distribui_cartas(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
    
    def aplicar_blinds(self):
        small_blind_player = self.obter_jogador_por_role("small_blind")
        big_blind_player = self.obter_jogador_por_role("big_blind")

        small_blind_valor = 5
        big_blind_valor = 10

        small_blind_player.pagar(small_blind_valor)
        big_blind_player.pagar(big_blind_valor)

        self.pot += small_blind_valor
        self.pot += big_blind_valor

        self.aposta_atual = big_blind_valor

        small_blind = [small_blind_player.name, 
                       small_blind_player.chips, 
                       self.pot,
                       self.aposta_atual]
        big_blind = [big_blind_player.name,
                     big_blind_player.chips,
                     self.pot,
                     self.aposta_atual]

        return small_blind, big_blind

    def flop(self):
        self.deck.draw_card()  # Queima
        self.community_cards = [self.deck.draw_card() for _ in range(2)]  # Flop

    def proxima_rodada(self):
        self.deck.draw_card()  # Queima
        self.community_cards.append(self.deck.draw_card())  # Turn/River

    def resetar_pote(self):
        self.pot = 0
    
    def resetar_aposta_atual(self):
        self.aposta_atual = 0
        for jogador in self.players:
            jogador.last_bet_made = 0

    def aplica_aposta(self, acao, jogador: Player):
        if jogador.active:
            if acao == "Fold":
                jogador.active = False
            elif acao == "Raise":
                novo_valor = self.aposta_atual + 10
                diferenca = novo_valor - jogador.last_bet_made
                jogador.pagar(diferenca)
                jogador.last_bet_made += diferenca
                self.aposta_atual = novo_valor
                self.pot += diferenca
            elif acao == "Call":
                diferenca = self.aposta_atual - jogador.last_bet_made
                jogador.pagar(diferenca)
                jogador.last_bet_made += diferenca
                self.pot += diferenca
            elif acao == "Check":
                pass
            
            return [jogador.name, acao, jogador.chips, self.pot, self.aposta_atual]

    def decide_acao_jogador_ia(self, jogador: Player):
        if jogador.active:
            if jogador.chips < self.aposta_atual:
                jogador.active = False

            acoes = []

            if self.aposta_atual == 0:
                acoes = ["Check", "Fold", "Fold"]
            else:
                acoes = ["Call", "Raise", "Fold"]

            escolha = random.choices(acoes, weights=[0.8, 0.15, 0.05])[0]
            return escolha
        
        else:
            return None
    
    def todos_igualaram_a_aposta(self, ordem_jogadores):
        for jogador in ordem_jogadores:
            if not jogador.active:
                continue
            if jogador.last_bet_made != self.aposta_atual:
                return False
        return True

    def escolhe_vencedor(self):
        melhor_mao = None
        vencedor = None

        for jogador in self.players:
            if jogador.active:
                result, mao_jogador = HandValue(jogador.hand, self.community_cards).calcular_forca()
                jogador.result = mao_jogador

                if (melhor_mao is None or
                    result[1] < melhor_mao[1] or
                    (result[1] == melhor_mao[1] and result[2] > melhor_mao[2])):
                    melhor_mao = result
                    vencedor = jogador
                    total = vencedor.chips + self.pot
                    vencedor.chips = total

        return vencedor.name, melhor_mao[0], melhor_mao[2], self.pot, vencedor.chips

    def obter_dados_jogadores(self):
        return {
            "jogadores": [
                {
                    "nome": player.name,
                    "role": player.role,
                    "cartas": [f"{card.rank} de {card.suit}" for card in player.hand]
                }
                for player in self.players
            ]
        }
    
    def obter_resultado_jogadores(self):
        return {
            "Resultado": [
                {
                    "nome": player.name,
                    "resultado": player.result
                }
                for player in self.players
            ]
        }
    
    def obter_dados_cartas_comunitarias(self):
        return {
            "comunitarias": [f"{card.rank} de {card.suit}" for card in self.community_cards]
        }