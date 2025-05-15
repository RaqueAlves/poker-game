from model.PokerGame import PokerGame
from view.TerminalView import TerminalView

class PokerGameController:
    def __init__(self, view: TerminalView):
        self.view = view
        self.jogo = None

    def iniciar_jogo(self):
        nome_usuario = self.view.solicitar_nome()
        self.jogo = PokerGame(nome_usuario)

        self.jogo.atualizar_posicoes()
        self.jogo.distribui_cartas()

        dados_jogadores = self.jogo.obter_dados_jogadores()
        self.view.mostrar_jogadores(dados_jogadores)

        # Pré-flop
        self.jogo.rodada_de_apostas()

        # Flop
        self.jogo.flop()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        self.jogo.rodada_de_apostas()

        # Turn
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        self.jogo.rodada_de_apostas()

        # River
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        self.jogo.rodada_de_apostas()

        # Final
        self.jogo.escolhe_vencedor()