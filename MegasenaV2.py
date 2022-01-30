import random

class Mega:
    def __init__(self,numjog,quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    def mostra_jogo(self):
        jogo = [random.sample(range(1, 61), self.quantinum) for i in range(self.numjog)]
        jogox = list(map(sorted, jogo))
        return jogox

    @classmethod
    def perg1(self):
        numjog = input('Quantos jogos vc quer fazer? (max 100 jogos)')
        quantinum = input("Vc quer jogo da MEGA SENA de quantos numeros?\ndigite 6, 7 ,8 ou 9: ")
        return self(int(numjog),int(quantinum))



jogo = Mega.perg1()
print(jogo.mostra_jogo())





