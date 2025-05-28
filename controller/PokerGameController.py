from model.PokerGame import PokerGame
from model.Player import Player
from view.TerminalView import TerminalView

class PokerGameController:
    def __init__(self, view: TerminalView):
        self.view = view
        self.jogo = None

    def iniciar_jogo(self):
        nome_usuario = self.view.iniciar_jogo()
        self.jogo = PokerGame(nome_usuario)

        self.jogo.atualizar_posicoes()
        self.jogo.distribui_cartas()

        self.view.mostrar_jogadores(self.jogo.obter_dados_jogadores())

        #Pré-flop
        self.primeira_rodada()
        self.jogo.flop()

        dicionario = {
            0 : "Flop",
            1 : "Turn",
            2 : "River"
        }
        #Flop, Turn e River
        for i in range(0, 3):
            print(f"\n=== {dicionario[i]} ===\n")
            self.jogo.proxima_rodada()
            self.view.mostrar_cartas_comunitarias(self.jogo.obter_dados_cartas_comunitarias())
            
            ordem = self.jogo.ordem_apostas()
            while True:
                for jogador in ordem:
                    if jogador.active:
                        self.rodada_de_apostas(jogador)
                if self.jogo.todos_igualaram_a_aposta(ordem) == True:
                    break
                
            self.jogo.resetar_aposta_atual()

        # Final
        jogador, combinacao, carta, pot, chips = self.jogo.escolhe_vencedor()
        self.view.mostrar_resultado(self.jogo.obter_resultado_jogadores())
        self.view.mostrar_vencedor([jogador, combinacao, carta, pot, chips])
    
    def primeira_rodada(self):
        # Pré-flop
        print("\n=== Pré Flop ===\n")
        small_blind, big_blind = self.jogo.aplicar_blinds()
        self.view.mostrar_blinds(small_blind, big_blind)
        
        ordem = self.jogo.ordem_apostas()

        while True:
            for jogador in ordem:
                self.rodada_de_apostas(jogador)
            if self.jogo.todos_igualaram_a_aposta(ordem) == True:
                break

        self.jogo.resetar_aposta_atual()
        
    def rodada_de_apostas(self, jogador: Player):
        if jogador.name not in ["Jogador 1", "Jogador 2", "Jogador 3"]:
            acao = self.view.coletar_acoes()
        else:
            acao = self.jogo.decide_acao_jogador_ia(jogador)

        if acao is not None:
            aposta = self.jogo.aplica_aposta(acao, jogador)
            self.view.mostrar_escolha_jogador(aposta)