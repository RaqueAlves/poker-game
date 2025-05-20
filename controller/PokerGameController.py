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
        acao = self.view.coletar_acoes()
        self.jogo.rodada_de_apostas(acao)

        # Flop
        self.jogo.flop()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao1 = self.view.coletar_acoes()
        self.jogo.rodada_de_apostas(acao1)

        # Turn
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao2 = self.view.coletar_acoes()
        self.jogo.rodada_de_apostas(acao2)

        # River
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao3 = self.view.coletar_acoes()
        self.jogo.rodada_de_apostas(acao3)

        # Final
        jogador, combinacao, carta, pot, chips = self.jogo.escolhe_vencedor()
        self.view.mostrar(f"\nVencedor: {jogador} com {combinacao} e carta mais alta: {carta}\n" \
              f"Ganhou {pot}fichas - Total: {chips}")