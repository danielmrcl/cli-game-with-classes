# Classes
class Personagem:
    def __init__(self, nome, andando=False, sentado=True):
        self.nome = nome
        self.andando = andando
        self.sentado = sentado

    def status(self):
        if self.sentado:
            posicao = "sentado"
        elif self.andando:
            posicao = "andando"
        elif not self.sentado and not self.andando:
            posicao = "parado"

        print(f"O jogador {self.nome} esta {posicao}.")

    def andar(self, direcao="frente"):
        if self.sentado:
            print(f"{self.nome} nao pode andar pois esta sentado")
        elif self.andando:
            print(f"{self.nome} ja esta andando")
        else:
            print(f"{self.nome} esta andando para {direcao}")
            self.andando = True

    def parar_andar(self):
        if self.andando:
            print(f"{self.nome} parou de andar")
            self.andando = False
        else:
            print(f"{self.nome} nao pode parar de andar pois nao esta andando")

    def sentar(self):
        if self.andando:
            print(f"{self.nome} nao pode sentar pois esta andando")
        elif self.sentado:
            print(f"{self.nome} ja esta sentado")
        else:
            print(f"{self.nome} sentou.")
            self.sentado = True

    def parar_sentar(self):
        if self.sentado:
            print(f"{self.nome} levantou")
            self.sentado = False
        else:
            print(f"{self.nome} nao pode se levantar pois nao esta sentado")
