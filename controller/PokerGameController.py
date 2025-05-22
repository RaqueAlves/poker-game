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

        self.view.mostrar_jogadores(self.jogo.obter_dados_jogadores())

        # Pré-flop
        small_blind, big_blind = self.jogo.aplicar_blinds()
        self.view.mostrar_blinds(small_blind, big_blind)
        acao = self.view.coletar_acoes()
        descricao = self.jogo.rodada_de_apostas(acao)
        self.view.mostrar_escolha_jogador(descricao)

        # Flop
        self.jogo.flop()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao1 = self.view.coletar_acoes()
        descricao1 = self.jogo.rodada_de_apostas(acao1)
        self.view.mostrar_escolha_jogador(descricao1)

        # Turn
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao2 = self.view.coletar_acoes()
        descricao2 = self.jogo.rodada_de_apostas(acao2)
        self.view.mostrar_escolha_jogador(descricao2)

        # River
        self.jogo.proxima_rodada()
        self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
        acao3 = self.view.coletar_acoes()
        descricao3 = self.jogo.rodada_de_apostas(acao3)
        self.view.mostrar_escolha_jogador(descricao3)

        # Final
        jogador, combinacao, carta, pot, chips = self.jogo.escolhe_vencedor()
        self.view.mostrar_resultado(self.jogo.obter_resultado_jogadores())
        self.view.mostrar(f"\nVencedor: {jogador} com {combinacao} e carta mais alta: {carta}\n" \
              f"Ganhou {pot}fichas - Total: {chips}")