from model.Player import Player
from model.Deck import Deck
from model.HandValue import HandValue

class PokerGame:
    def __init__(self, usuario):
        self.deck = Deck()
        self.players = [
            Player(usuario),
            Player("Alice"),
            Player("Bob"),
            Player("Carol")
        ]
        self.community_cards = []
        self.dealer_index = 0

    def iniciar_jogo(self):
        self.atualizar_posicoes()
        self.distribuir_cartas()
        self.distribuir_cartas_comunitarias()

    def atualizar_posicoes(self):
        num_players = len(self.players)
        for player in self.players:
            player.role = "normal"
        
        self.players[self.dealer_index].role = "dealer"
        self.players[(self.dealer_index + 1) % num_players].role = "small_blind"
        self.players[(self.dealer_index + 2) % num_players].role = "big_blind"

        self.dealer_index = (self.dealer_index + 1) % num_players

    def distribuir_cartas(self):
        for player in self.players:
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]

    def distribuir_cartas_comunitarias(self):
        self.deck.draw_card()  # Queima
        self.community_cards = [self.deck.draw_card() for _ in range(3)]  # Flop

        self.deck.draw_card()  # Queima
        self.community_cards.append(self.deck.draw_card())  # Turn

        self.deck.draw_card()  # Queima
        self.community_cards.append(self.deck.draw_card())  # River

    def escolhe_vencedor(self):
        melhor_mao = None
        vencedor = None

        for jogador in self.players:
            resultado = HandValue(jogador.hand, self.community_cards).calcular_forca()
            print(f"{jogador.name}: {resultado}")  # Para depuração

            if (melhor_mao is None or
                resultado[1] < melhor_mao[1] or
                (resultado[1] == melhor_mao[1] and resultado[2] > melhor_mao[2])):
                melhor_mao = resultado
                vencedor = jogador

        print(f"\nVencedor: {vencedor.name} com {melhor_mao[0]} (carta mais alta: {melhor_mao[2]})")

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