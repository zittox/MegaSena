# MEGA SENA -

import random
import time

class Mega:

    quantinum = int()
    numjog = int()

    def __init__(self,numjog,quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    @classmethod
    def mostra_jogo(self):
        jogo = [random.sample(range(1, 61), self.quantinum) for i in range(self.numjog)]
        jogox = ""
        while jogo:
            for i in jogo:
                i.sort()
                jogox = "\n".join(str(i) for i in jogo)
            break

        if self.numjog == 1:
            print(f'O jogo de {self.quantinum} números é :\n{jogox}')
        else:
            print(f'Os {self.numjog} jogos de {self.quantinum} números são:\n\nCALCULAND0 ~~~~ └[∵┌]└[ ∵ ]┘[┐∵]┘\n')
            time.sleep(2)
            print(f'{jogox}\n\n_/\_ Boa sorte!')


    @classmethod
    def perg1(self):
         while True:
            self.quantinum = input("\n\nQuantos números tem o jogo da MEGA SENA que você quer?\ndigite uma opção: 6, 7, 8 ou 9\n")
            try:
                self.quantinum = int(self.quantinum)
                if self.quantinum == 6 or self.quantinum == 7 or self.quantinum == 8 or self.quantinum == 9:
                    print("\n~~~~>> Você escolheu ter", self.quantinum, "números em cada jogo ----~!~~!~~!\n")
                    break
                elif self.quantinum != range(6,10):
                    print("\n!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!\n")
                    self.perg1()
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                self.perg1()
            return int(self.quantinum)


    @classmethod
    def perg2(self):

        while True:
            self.numjog = int(input(f"Quantos jogos você gostaria de ter com {self.quantinum} números?\n"))
            try:

                if self.numjog > 100:
                    print("O máximo são 100 jogadas <<<--------")
                elif self.numjog >= 1 and self.numjog <= 100:
                    print(f"\n~~~~>> Você escolheu  {self.numjog} jogos\n")

            except ValueError:
                print("Digite umnúmero")
            break
        return int(self.numjog)





Mega.perg1()
Mega.perg2()
Mega.mostra_jogo()






