from controller.PokerGame import PokerGame
from view.terminal import TerminalView

from controller.PokerGame import PokerGame
from view.terminal import TerminalView

def main():
    view = TerminalView()

    nome_usuario = view.solicitar_nome()
    jogo = PokerGame(nome_usuario)

    jogo.iniciar_jogo()
    dados1 = jogo.obter_dados_jogadores()
    dados2 = jogo.obter_dados_cartas_comunitarias()
    view.mostrar_jogadores(dados1)
    view.mostrar_cartas_comunitarias(dados2)

if __name__ == "__main__":
    main()

