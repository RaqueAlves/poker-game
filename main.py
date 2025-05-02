from controller.PokerGame import PokerGame
from view.terminal import TerminalView

from controller.PokerGame import PokerGame
from view.terminal import TerminalView

def main():
    view = TerminalView()

    nome_usuario = view.solicitar_nome()
    jogo = PokerGame(nome_usuario)

    jogo.iniciar_jogo()
    dados = jogo.obter_dados_jogadores()
    view.mostrar_jogadores(dados)

if __name__ == "__main__":
    main()

