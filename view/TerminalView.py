import time

class TerminalView:
    def mostrar_jogador(self, dados, is_human):
        cartas = []

        if is_human:
            print(f"\n\033[92mNome: {dados['nome']}")
            print(f"Cargo: {dados['role']}")
            for carta in dados["cartas"]:
                cartas.append(carta)
            print(f"Cartas: {cartas}\033[0m")
        
        else:
            print(f"\nNome: {dados['nome']}")
            print(f"Cargo: {dados['role']}")
            for carta in dados["cartas"]:
                cartas.append(carta)
            print(f"Cartas: {cartas}")
        
        time.sleep(1)
        cartas.clear()

    def mostrar_cartas_comunitarias(self, dados):
        time.sleep(1)
        print("\n=== Cartas Comunitárias ===")
        for carta in dados["comunitarias"]:
            print(f"  - {carta}")
        print()
        time.sleep(1)

    def mostrar_escolha_jogador(self, dados, is_human):
        if is_human:
            print(f"\033[92m{dados[0]} escolheu: {dados[1]}\n"
                    f"Fichas restantes: {dados[2]} |"
                    f"Pote atual: {dados[3]} | "
                    f"Aposta atual: {dados[4]} | \033[0m")
            time.sleep(1)
        
        else:
            print(f"{dados[0]} escolheu: {dados[1]}\n"
                    f"Fichas restantes: {dados[2]} |"
                    f"Pote atual: {dados[3]} | "
                    f"Aposta atual: {dados[4]} | ")
            time.sleep(1)
    
    def mostrar_resultado(self, dados):
        time.sleep(1)
        print("\n=== Mãos dos Jogadores ===")
        for resultado in dados["Resultado"]:
            print(f"Nome: {resultado["nome"]}")
            print(f"Mão: {resultado["resultado"]}")
            print(f"Combinação: {resultado["combinacao"]}\n")
            time.sleep(1)
    
    def mostrar_blinds(self, small_blind, big_blind):
        print("\n=== Pagamento dos Blinds ===")
        time.sleep(1)
        print(f"\nSmall Blind {small_blind[0]}: pagou 5 fichas\n"
                f"Fichas restantes: {small_blind[1]} |"
                f"Pote atual: {small_blind[2]} | "
                f"Aposta atual: {small_blind[3]} | ")
        time.sleep(1)
        print(f"Big Blind {big_blind[0]}: pagou 10 fichas\n"
                f"Fichas restantes: {big_blind[1]} |"
                f"Pote atual: {big_blind[2]} | "
                f"Aposta atual: {big_blind[3]} | ")
        time.sleep(1)
    
    def coletar_acoes(self):
        dicionario = {
            "1": "Check",
            "2": "Call",
            "3": "Raise",
            "4": "Fold"
        }
        print("\n=== Rodada de Apostas ===\n" \
        "1. Check(Passar)\n" \
        "2. Call(Pagar)\n" \
        "3. Raise(Aumentar)\n" \
        "4. Fold(Desistir)\n")

        while True:
            choose = input()
            if choose in ["1", "2", "3", "4"]:
                return dicionario[choose]
            else:
                print("Escolha inválida!")
    
    def mostrar_vencedor(self, dados):
        time.sleep(1)
        print(f"\n🏆 VENCEDOR 🏆\n"
              f"{dados[0]} venceu com: {dados[1]}\n"
              f"Carta mais alta: {dados[2]}\n"
              f"Ganhou: {dados[3]} fichas!\n"
              f"Total de fichas: {dados[4]}\n")
    
    def iniciar_jogo(self):
        print("♠️♥️ Bem-vindo ao Poker Terminal!\n" 
              "O jogo já vai começar... ♣️♦️\n")
        time.sleep(1)
        return input("Digite seu nome antes de iniciar: ")
    
    def mostrar(self, mensagem):
        print(mensagem)
        time.sleep(1)