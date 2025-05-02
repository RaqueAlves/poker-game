from model.Player import Player

class PokerGame:
    def __init__(self, players: list):
        self.players = players
        self.dealer_index = 0
    
    @property
    def players(self):
        return self.__players
    
    @players.setter
    def players(self, players):
        if not isinstance(players, list):
            raise TypeError("players deve ser uma lista.")
        
        for player in players:
            if not isinstance(player, Player):
                raise TypeError("player deve ser um objeto da classe Player.")
            
        self.__players = players

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
