
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self.__rank
    
    @rank.setter
    def rank(self, rank):
        if not isinstance(rank, str):
            raise TypeError('Rank deve ser do tipo str.')
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    
    @suit.setter
    def suit(self, suit):
        if not isinstance(suit, str):
            raise TypeError('suit deve ser do tipo str.')
        self.__suit = suit

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def get_value(self):
        """Retorna o valor da carta para fins de Blackjack."""
        if self.rank == 'J':
            return 11
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'K':
            return 13
        elif self.rank == 'A':
            return 14
        else:
            return int(self.rank)
        
    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return self.__str__()