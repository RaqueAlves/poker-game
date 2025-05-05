from model.PokerGame import PokerGame

class PokerGameController:
    def __init__(self, nome_usuario):
        self.jogo = PokerGame(nome_usuario)

    def iniciar_jogo(self):
        self.jogo.atualizar_posicoes()
        self.jogo.distribui_cartas()