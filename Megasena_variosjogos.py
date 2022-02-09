# MEGA SENA ____  Gerador aleatório de jogos
# por: github.com/zittox-

import random
import time


class Mega:
    quantinum = int()
    numjog = int()

    def __init__(self, numjog, quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    @classmethod
    def mostra_jogo(self):
        jogo = [random.sample(range(1, 61), self.quantinum) for i in range(self.numjog)]
        while jogo:
            for i in jogo:
                i.sort()
            break
        jogo.sort()
        jogox = ""
        while jogo:
            for i in jogo:
                i.sort()
                jogox = "\n".join(str(i) for i in jogo)
            break

        if self.numjog == 1:
            print(f'O jogo de {self.quantinum} números é :\n{jogox}')
            self.pergunta_sim_nao("Gostaria de continuar?")
        else:
            print(f'Os {self.numjog} jogos de {self.quantinum} números são:\n\nCALCULAND0 ~~~~ └[∵┌]└[ ∵ ]┘[┐∵]┘\n')
            time.sleep(2)
            print(f'{jogox}\n')
            self.pergunta_sim_nao("Gostaria de continuar?")

    @classmethod
    def perg1(self):
        while True:
            self.quantinum = input(
                "\nQuantos números tem o jogo da MEGA SENA que você quer?\ndigite uma opção: 6, 7, 8 ou 9\n")
            try:
                self.quantinum = int(self.quantinum)
                if self.quantinum == 6 or self.quantinum == 7 or self.quantinum == 8 or self.quantinum == 9:
                    print(f"\n~~~~>> Você escolheu ter {self.quantinum} números em cada jogo ----~!~~!~~!\n")
                    break
                elif self.quantinum != range(6, 10):
                    print("\n!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!")
                    self.perg1()
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                self.perg1()
            return self.quantinum

    @classmethod
    def perg2(self):

        while True:
            self.numjog = input(f"Quantos jogos você gostaria de ter com {self.quantinum} números?\n")
            try:
                self.numjog = int(self.numjog)
                if self.numjog > 100:
                    print("\nO máximo são 100 jogadas <<<--------\n")
                    self.perg2()
                elif 1 <= self.numjog <= 100:
                    print(f"\n~~~~>> Você escolheu {self.numjog} jogos\n")
                break
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: digite um número entre 1 e 100 <<<< !!!!\n")
                self.perg2()

            return self.numjog

    @classmethod
    def pergunta_sim_nao(self, menssagem):

        resposta = ""
        while resposta not in ("s", "n"):
            resposta = input(f"\n{menssagem} (s ou n):")
            if resposta not in ("s", "n"):
                print("\nPor favor, digite sim \"s\" ou não \"n\"")
            elif resposta == "n":
                print("\n__ Boa sorte!\n >>>>> Até a próxima!!!")
                break
            else:
                self.perg1()
                self.perg2()
                self.mostra_jogo()


Mega.pergunta_sim_nao(" ~~~~~~ Bem vindo ____\nGostaria de fazer jogo(s) da Mega Sena?")
