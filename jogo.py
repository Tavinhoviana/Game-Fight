import random
# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhe(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)  # baseado no nivel
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} Atacou {alvo.get_nome()} e causou {dano} de dano")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) # Dano aumentado
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    """ Classe orquestradora do jogo """

    def __init__(self):
        self.heroi = Heroi(nome="Guinga", vida=100, nivel=5, habilidade="Super força")
        self.inimigo = Inimigo (nome="Djalma", vida=80, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """ Fazer a gestao da batalha em turnos """
        print("Iniciando a batalha!")   
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhe())
            print(self.inimigo.exibir_detalhe())

            input("Pressione ENTER para atacar... ")
            escolha = input("Escolha (1 = Ataque Normal, 2 = Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                #Inimigo ataca o heroi.
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabens voce venceu a batalha!")
        else:
            print("Voce foi derrotado!")


# Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()


# heroi = Heroi(nome="Guinga", vida=100, nivel=5, habilidade="Super força")
# print(heroi.exibir_detalhe())
# Inimigo = Inimigo (nome="Djalma", vida=50, nivel=3, tipo="Voador")
# print(Inimigo.exibir_detalhe())