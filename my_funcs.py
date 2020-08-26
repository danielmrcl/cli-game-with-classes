# Funções:
from os import system

def pegar_nome_jogador():
    while True:
        nome = str(input("Nome do jogador: ")).strip().title()

        if ' ' in nome:
            print("[ERRO] o nome do jogador nao pode conter espacos, tente outro...")
            continue

        try:
            confirmar = str(input(f"Confirmar nome ({nome})? [s/N]: "))[0].upper().strip()
        except IndexError:
            confirmar = ''

        if confirmar == 'S':
            break

        print("Escolha outro nome...")
    return nome

def jogar(player):
    while True:
        print("Status do personagem:")
        player.status()

        print("\nDigite um movimento para o personagem:")
        print("[1] Andar\n[2] Sentar\n[3] Parar de andar\n[4] Levantar\n[0] Sair do jogo")

        movimento = str(input(">>> ")).strip().replace(' ', '')

        if movimento == '1':
            direcao = str(input("Digite para qual direcao [FRENTE/direita/esquerda/tras]:")).replace(' ', '')

            if len(direcao) == 0:
                player.andar()
            else:
                player.andar(direcao)

        elif movimento == '2':
            player.sentar()

        elif movimento == '3':
            player.parar_andar()

        elif movimento == '4':
            player.parar_sentar()

        elif movimento == '0':
            break

        else:
            print("Movimento nao aceito digite novamente...")

        input("\n=== Digite enter para continuar ===\n")


        system("clear")

def creditos():
    system("clear")
    print(
    "Este jogo foi criado em 07/2020 por:\n",
    "Daniel M. S. Junior - Estudante de Analise e Des. de Sistemas - 3 periodo\n",
    "Contato:\ttwitter.com/danielsmrcl\n",
    )
