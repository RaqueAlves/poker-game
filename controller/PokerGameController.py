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
        self.rodada_de_apostas()
        self.jogo.resetar_aposta_atual()

        for i in range(0, 2):
            # Flop
            self.jogo.flop()
            self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
            self.rodada_de_apostas()
            self.jogo.resetar_aposta_atual()

        # Final
        jogador, combinacao, carta, pot, chips = self.jogo.escolhe_vencedor()
        self.view.mostrar_resultado(self.jogo.obter_resultado_jogadores())
        self.view.mostrar(f"\nVencedor: {jogador} com {combinacao} e carta mais alta: {carta}\n" \
              f"Ganhou {pot}fichas - Total: {chips}")
        
    def rodada_de_apostas(self):
        ordem = self.jogo.ordem_apostas()

        for jogador in ordem:
            if jogador.name not in ["Jogador 1", "Jogador 2", "Jogador 3"]:
                acao = self.view.coletar_acoes()
            else:
                acao = self.jogo.decide_acao_jogador_ia(jogador)

            if acao is not None:
                aposta = self.jogo.aplica_aposta(acao, jogador)
                self.view.mostrar_escolha_jogador(aposta)