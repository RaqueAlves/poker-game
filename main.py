from model.PokerGame import PokerGame
from model.Player import Player

players = [Player("Alice"), Player("Bob"), Player("Carol"), Player("Dan")]
game = PokerGame(players)

for i in range(4):
    print(f"\n--- Mão {i+1} ---")
    game.atualizar_posicoes()
    for p in players:
        print(f"{p.name} → {p.role}")
