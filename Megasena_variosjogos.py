# MEGA SENA ____  Gerador aleatório de jogos
# por: github.com/zittox
# colaborador: github.com/ozzysp

import random
import time


class Mega:
    quantinum = int()
    numjog = int()

    def __init__(self, numjog, quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    @classmethod
    def mostra_jogo(cls):
        jogo = [random.sample(range(1, 61), cls.quantinum) for _ in range(cls.numjog)]
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

        if cls.numjog == 1:
            print(f'O jogo de {cls.quantinum} números é :\n{jogox}')
            cls.pergunta_sim_nao("Gostaria de continuar?")
        else:
            print(f'Os {cls.numjog} jogos de {cls.quantinum} números são:\n\nCALCULAND0 ~~~~ └[∵┌]└[ ∵ ]┘[┐∵]┘\n')
            time.sleep(2)
            print(f'{jogox}\n')
            cls.pergunta_sim_nao("Gostaria de continuar?")

    @classmethod
    def perg1(cls):
        while True:
            cls.quantinum = input(
                "\nQuantos números tem o jogo da MEGA SENA que você quer?\ndigite uma opção: 6, 7, 8 ou 9\n")
            try:
                cls.quantinum = int(cls.quantinum)
                if cls.quantinum == 6 or cls.quantinum == 7 or cls.quantinum == 8 or cls.quantinum == 9:
                    print(f"\n~~~~>> Você escolheu ter {cls.quantinum} números em cada jogo ----~!~~!~~!\n")
                    break
                elif cls.quantinum != range(6, 10):
                    print("\n!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!")
                    cls.perg1()
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                cls.perg1()
            return cls.quantinum

    @classmethod
    def perg2(cls):

        while True:
            cls.numjog = input(f"Quantos jogos você gostaria de ter com {cls.quantinum} números?\n")
            try:
                cls.numjog = int(cls.numjog)
                if cls.numjog > 100:
                    print("\nO máximo são 100 jogadas <<<--------\n")
                    cls.perg2()
                elif 1 <= cls.numjog <= 100:
                    print(f"\n~~~~>> Você escolheu {cls.numjog} jogos\n")
                break
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: digite um número entre 1 e 100 <<<< !!!!\n")
                cls.perg2()

            return cls.numjog

    @classmethod
    def pergunta_sim_nao(cls, menssagem):

        resposta = ""
        while resposta not in ("s", "n"):
            resposta = input(f"\n{menssagem} (s ou n): ")
            if resposta not in ("s", "n"):
                print("\nPor favor, digite sim \"s\" ou não \"n\"")
            elif resposta == "n":
                print("\n__ Boa sorte!\n >>>>> Até a próxima!!!")
                break
            else:
                cls.perg1()
                cls.perg2()
                cls.mostra_jogo()


Mega.pergunta_sim_nao(" ~~~~~~ Bem vindo ____\nGostaria de fazer jogo(s) da Mega Sena?")
