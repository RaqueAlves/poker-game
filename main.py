from model.PokerGame import PokerGame
from view.TerminalView import TerminalView

from model.PokerGame import PokerGame
from view.TerminalView import TerminalView

from controller.PokerGameController import PokerGameController

def main():
    view = TerminalView()
    nome_usuario = view.solicitar_nome()

    jogo = PokerGame(nome_usuario)
    jogo.atualizar_posicoes()
    jogo.distribui_cartas()
    dados1 = jogo.obter_dados_jogadores()
    view.mostrar_jogadores(dados1)
    jogo.rodada_de_apostas()
    jogo.flop()
    dados3 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados3)
    jogo.rodada_de_apostas()
    jogo.proxima_rodada()
    dados4 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados4)
    jogo.rodada_de_apostas()
    jogo.proxima_rodada()
    dados5 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados5)
    jogo.rodada_de_apostas()

    jogo.escolhe_vencedor()

if __name__ == "__main__":
    main()