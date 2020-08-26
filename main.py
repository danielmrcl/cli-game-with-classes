# Python Classes e Objetos
import os
import my_funcs
from my_classes import Personagem

def main():
    print("=== Criando personagem ===")
    player_nome = my_funcs.pegar_nome_jogador()

    player1 = Personagem(player_nome)

    print("=== Tudo pronto para comecar ===")

    input("Digite ENTER para para jogar... ")
    os.system("clear")

    # Jogar
    my_funcs.jogar(player1)


if __name__ == "__main__":
    os.system("clear")
    main()
    print("\n=== Obrigado por jogar meu joguinho :D ===")
    print("\n=== digite ENTER para realmente sair ou 1 para ver os creditos ===")
    if len(str(input()).strip()) != 0:
        my_funcs.creditos()
