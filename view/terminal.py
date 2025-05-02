class TerminalView:
    def mostrar_jogadores(self, dados):
        print("\n=== Jogadores e suas cartas ===")
        for jogador in dados["jogadores"]:
            print(f"\nNome: {jogador['nome']}")
            print(f"Cargo: {jogador['role']}")
            print("Cartas:")
            for carta in jogador["cartas"]:
                print(f"  - {carta}")

        print("\n=== Cartas Comunitárias ===")
        for carta in dados["comunitarias"]:
            print(f"  - {carta}")
    
    def solicitar_nome(self):
        return input("Digite seu nome antes de iniciar: ")