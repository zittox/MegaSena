# MEGA SENA -

import random

class Mega:

    quantinum = None
    numjog = None

    def __init__(self,numjog,quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    @classmethod
    def mostra_jogo(self):

        jogo = [random.sample(range(1, 61), self.quantinum) for i in range(self.numjog)]
        jogox = list(map(sorted, jogo))
        if self.numjog == 1:
            print(f'O jogo é: ' + str(jogox))
        else:
            print(f'Os jogos são: ' + str(jogox))
        return jogox

    @classmethod
    def perg1(self):
        while True:
            self.quantinum = input("Vc quer jogo da MEGA SENA de quantos numeros?\ndigite 6, 7 ,8 ou 9: ")
            try:
                self.quantinum = int(self.quantinum)
                if self.quantinum != 6 or self.quantinum != 7 or self.quantinum != 8 or self.quantinum != 9:
                    print("Escolha um numero entre 6 e 9")

            except ValueError:
                print("\nPRESTENÇÃO: Favor escolher um numero")

            self.numjog = input('Digite o numero de jogos que gostaria?\n')
            try:

                self.numjog = int(self.numjog)

                if self.numjog > 100:
                    print("O máximo são 100 jogadas.")
                elif self.numjog >= 1 and self.numjog <= 100:
                    print("Você escolheu", self.numjog, "jogos")

            except ValueError:
                print("Digite um numero")

            break

        return int(self.numjog),int(self.quantinum)





x = Mega.perg1()
y = Mega.mostra_jogo()






