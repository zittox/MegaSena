import random
import time

perg = input("Vc quer fazer um jogo da MEGAENA de quantos numeros?\ndigite 6, 7 ,8 ou 9: ")


def jogo():
    sair = False
    while not sair:
        if perg == "6":
            l6 = random.sample(range(1, 61), 6)
            l6.sort()
            print("\ncalculando~~└[∵┌]└[ ∵ ]┘[┐∵]┘")
            time.sleep(1)
            print(l6)
            sair = pergunta_sim_nao("\nOutro jogo?")
        if perg == "7":
            l7 = random.sample(range(1, 61), 7)
            l7.sort()
            print("\ncalculando~~└[∵┌]└[ ∵ ]┘[┐∵]┘")
            time.sleep(1)
            print(l7)
            sair = pergunta_sim_nao("\nOutro jogo?")
        if perg == "8":
            l8 = random.sample(range(1, 61), 8)
            l8.sort()
            print("\ncalculando~~└[∵┌]└[ ∵ ]┘[┐∵]┘")
            time.sleep(1)
            print(l8)
            sair = pergunta_sim_nao("\nOutro jogo?")
        if perg == "9":
            l9 = random.sample(range(1, 61), 9)
            l9.sort()
            print("\ncalculando~~└[∵┌]└[ ∵ ]┘[┐∵]┘")
            time.sleep(1)
            print(l9)
            sair = pergunta_sim_nao("\nOutro jogo?")


def pergunta_sim_nao(mensagem):
    resposta = ""
    while resposta not in ("s", "n"):
        resposta = input(mensagem + " (s ou n): ")
        if resposta not in ("s", "n"):
            print("\nPor favor, digite sim \"s\" ou não \"n\"")
    return resposta == "n"


jogo()
