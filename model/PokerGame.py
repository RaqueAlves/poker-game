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
        for player in self.players:
            player.role = "normal"
        
        self.players[self.dealer_index].role = "dealer"
        self.players[(self.dealer_index + 1) % num_players].role = "small_blind"
        self.players[(self.dealer_index + 2) % num_players].role = "big_blind"

        self.dealer_index = (self.dealer_index + 1) % num_players

    def shuffle(self):
        random.shuffle(self.players)

    def distribui_cartas(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def flop(self):
        self.deck.draw_card()  # Queima
        self.community_cards = [self.deck.draw_card() for _ in range(3)]  # Flop

    def proxima_rodada(self):
        self.deck.draw_card()  # Queima
        self.community_cards.append(self.deck.draw_card())  # Turn/River
    
    def adicionar_ao_pote(self, fichas):
        self.pot += fichas

    def resetar_pote(self):
        self.pot = 0

    def rodada_de_apostas(self, acao):
        print(acao)
        for jogador in self.players:
            print(acao)
            if jogador.active:
                print(acao)
                if jogador.name not in ["Jogador 1", "Jogador 2", "Jogador 3"]:
                    print(acao)
                    if acao == "5":
                        jogador.active = False
                    elif acao == "4":
                        self.aposta_atual += 10
                        jogador.pagar(self.aposta_atual)
                        self.adicionar_ao_pote(self.aposta_atual)
                    elif acao == "3" or acao == "2":
                        jogador.pagar(self.aposta_atual)
                        self.adicionar_ao_pote(self.aposta_atual)
                    elif acao == "1":
                        pass

                    print(f"Escolha de {jogador.name}: {acao}")
                    print(f"Fichas no Pote: {self.pot}")
                    print(f"Valor da aposta atual: {self.aposta_atual}\n")
                else:
                    acao_ia = self.decidir_acao_jogador_ia(jogador)
                    print(f"Escolha de {jogador.name}: {acao_ia}")
                    print(f"Fichas no Pote: {self.pot}")
                    print(f"Valor da aposta atual: {self.aposta_atual}\n")

    def decidir_acao_jogador_ia(self, jogador: Player):
        if jogador.chips < self.aposta_atual:
            jogador.active = False

        acoes = []

        if self.aposta_atual == 0:
            acoes = ["check", "bet", "fold"]
        else:
            acoes = ["call", "raise", "fold"]

        escolha = random.choices(acoes, weights=[0.8, 0.15, 0.05])[0]

        if escolha == "fold":
            jogador.active = False
            return escolha
        elif escolha == "bet":
            jogador.pagar(10)
            self.adicionar_ao_pote(10)
            self.aposta_atual += 10
            return escolha
        elif escolha == "check":
            return escolha
        elif escolha == "call":
            jogador.pagar(self.aposta_atual)
            self.adicionar_ao_pote(self.aposta_atual)
            return escolha
        elif escolha == "raise":
            self.aposta_atual += 10
            jogador.pagar(self.aposta_atual)
            self.adicionar_ao_pote(self.aposta_atual)
            return escolha

    def escolhe_vencedor(self):
        melhor_mao = None
        vencedor = None

        for jogador in self.players:
            if jogador.active:
                resultado = HandValue(jogador.hand, self.community_cards).calcular_forca()
                print(f"{jogador.name}: {resultado}")

                if (melhor_mao is None or
                    resultado[1] < melhor_mao[1] or
                    (resultado[1] == melhor_mao[1] and resultado[2] > melhor_mao[2])):
                    melhor_mao = resultado
                    vencedor = jogador
                    print(jogador.chips)
                    total = vencedor.chips + self.pot
                    vencedor.chips = total

        print(f"\nVencedor: {vencedor.name} com {melhor_mao[0]} e carta mais alta: {melhor_mao[2]}\n" \
              f"Ganhou {self.pot}fichas - Total: {jogador.chips}")

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
    
    def obter_dados_cartas_comunitarias(self):
        return {
            "comunitarias": [f"{card.rank} de {card.suit}" for card in self.community_cards]
        }