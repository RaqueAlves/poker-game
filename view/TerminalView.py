class TerminalView:
    def mostrar_jogadores(self, dados):
        print("\n=== Jogadores e suas cartas ===")
        for jogador in dados["jogadores"]:
            print(f"\nNome: {jogador['nome']}")
            print(f"Cargo: {jogador['role']}")
            print("Cartas:")
            for carta in jogador["cartas"]:
                print(f"  - {carta}")

    def mostrar_cartas_comunitarias(self, dados):
        print("\n=== Cartas Comunitárias ===")
        for carta in dados["comunitarias"]:
            print(f"  - {carta}")
    
    def coletar_acoes(self):
        dicionario = {
            "1": "Check",
            "2": "Bet",
            "3": "Call",
            "4": "Raise",
            "5": "Fold"
        }
        print("\n=== Rodada de Apostas ===\n" \
        "1. Check(Passar)\n" \
        "2. Bet(Apostar)\n" \
        "3. Call(Pagar)\n" \
        "4. Raise(Aumentar)\n" \
        "5. Fold(Desistir)\n")
        choose = input()
        if choose in ["1", "2", "3", "4", "5"]:
            return dicionario[choose]
    
    def solicitar_nome(self):
        return input("Digite seu nome antes de iniciar: ")