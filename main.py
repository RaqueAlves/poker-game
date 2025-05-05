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
    d1 = view.mostrar_opcoes_de_apostas()
    jogo.rodada_de_apostas(d1)
    jogo.flop()
    dados3 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados3)
    d2 = view.mostrar_opcoes_de_apostas()
    jogo.rodada_de_apostas(d2)
    jogo.proxima_rodada()
    dados4 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados4)
    d3 = view.mostrar_opcoes_de_apostas()
    jogo.rodada_de_apostas(d3)
    jogo.proxima_rodada()
    dados5 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_cartas_comunitarias(dados5)
    d4 = view.mostrar_opcoes_de_apostas()
    jogo.rodada_de_apostas(d4)

    jogo.escolhe_vencedor()

if __name__ == "__main__":
    main()