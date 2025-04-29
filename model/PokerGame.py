class PokerGame:
    def __init__(self, players):
        self.players = players
        self.dealer_index = 0

    def atualizar_posicoes(self):
        num_players = len(self.players)
        
        # Zera os roles anteriores
        for player in self.players:
            player.role = "normal"
        
        self.players[self.dealer_index].role = "dealer"
        self.players[(self.dealer_index + 1) % num_players].role = "small_blind"
        self.players[(self.dealer_index + 2) % num_players].role = "big_blind"

        # Avança o dealer para a próxima mão
        self.dealer_index = (self.dealer_index + 1) % num_players
