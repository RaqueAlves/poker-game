from model.PokerGame import PokerGame
from view.TerminalView import TerminalView

from model.PokerGame import PokerGame
from view.TerminalView import TerminalView

from controller.PokerGameController import PokerGameController

def main():
    view = TerminalView()
    controller = PokerGameController(view)
    controller.iniciar_jogo()

if __name__ == "__main__":
    main()