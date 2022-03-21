# MEGA SENA ____  Gerador aleatório de jogos
# por: github.com/zittox
# colaborador: github.com/ozzysp
# api de resultados: github.com/guto-alves/loterias-api


import time
import qrandom
import requests



class Mega:

    def __init__(self, numjog, quantinum):
            self.numjog = numjog
            self.quantinum = quantinum

    def perg1():
        while True:
            quantinum = input("\nQuantos números tem o jogo da MEGA SENA que você quer?\ndigite uma opção: 6, 7, 8 ou 9\n")
            try:
                quantinum = int(quantinum)
                if quantinum >= 6 < 10:
                    print(f"\n~~~~>> Você escolheu ter {quantinum} números em cada jogo ----~!~~!~~!\n")
                    break
                else:
                    print("\n!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!")
                    Mega.perg1()
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                Mega.perg1()
            return quantinum

        def perg2():
            while True:
                numjog = input(f"Quantos jogos você gostaria de ter com {quantinum} números?\n")
                try:
                    numjog = int(numjog)
                    if numjog == 0:
                        print("\n!!!!! >>>> ZERO jogadas não é um número válido neh, tenta de novo! <<<< !!!!\n")
                        Mega.perg2()
                    if numjog > 100:
                        print("\nO máximo são 100 jogadas <<<--------\n")
                        Mega.perg2()
                    elif numjog >= 1 and numjog <= 100:
                        print(f"\n~~~~>> Você escolheu {numjog} jogos\n")
                    break
                except ValueError:
                    print("\n!!!!! >>>> PRESTENÇÃO: digite um número entre 1 e 100 <<<< !!!!\n")
                    Mega.perg2()
                return numjog

            def mostra_jogo():
                jogo2 = [qrandom.sample(range(1, 61), quantinum) for _ in range(numjog)]

                while jogo2:
                    for i in jogo2:
                        i.sort()
                    break
                jogo2.sort()

                jogox2 = ""
                while jogo2:
                    for i in jogo2:
                        i.sort()
                        jogox2 = "\n".join(str(i) for i in jogo2)
                    break

                if numjog == 1:
                    print(f'O jogo de {quantinum} número é :\n{jogox2}')
                    pergunta_sim_nao("Gostaria de continuar?\n")
                else:
                    print(f'Os {numjog} jogos de {quantinum} números são:\n\nCALCULAND0 ~~~~ └[∵┌]└[ ∵ ]┘[┐∵]┘\n')
                    time.sleep(2)
                    print(f'{jogox2}\n')
                    pergunta_sim_nao("Gostaria de continuar?\n")
            mostra_jogo()
        perg2()


class Result:

    def ultimo_resultado():
        apicaixa = 'https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest'
        r = requests.get(apicaixa).json()
        data = f"Concurso: {r['concurso']}"
        data1 = f"Data: {r['data']}"
        data2 = f"Dezenas: {r['dezenas']}"
        if r['premiacoes'][0]['vencedores'] == 0:
            venc = f"Vencedores: Não"
        else:
            venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}"
        if r['premiacoes'][0]['premio'] == "-":
            prem = f"Premiações: 0"
        else:
            prem = f"Premiações: R$ {r['premiacoes'][0]['premio']}"
        if r['acumulou'] == True:
            data3 = "Acumulou: Sim"
        else:
            data3 = "Acumulou: Não"
        data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
        data5 = f"Prox_concurso: {r['dataProxConcurso']}"
        print(f'{data}\n{data1}\n{data2}\n{venc}\n{prem}\n{data3}\n{data4}\n{data5}')
        pergunta_sim_nao("Gostaria de continuar?")

    def qual_concurso():
        conc = input("Digite o número do concurso que deseja pesquisar:\n")
        apicaixaconc = f'https://loteriascaixa-api.herokuapp.com/api/mega-sena/{conc}'
        r = requests.get(apicaixaconc).json()
        data = f"Concurso: {r['concurso']}"
        data1 = f"Data: {r['data']}"
        data2 = f"Dezenas: {r['dezenas']}"
        if r['premiacoes'][0]['vencedores'] == 0:
            venc = f"Vencedores: Não"
        else:
            venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}"
        if r['premiacoes'][0]['premio'] == "-":
            prem = f"Premiações: 0"
        else:
            prem = f"Premiações: R$ {r['premiacoes'][0]['premio']}"
        if r['acumulou'] == True:
            data3 = "Acumulou: Sim"
        else:
            data3 = "Acumulou: Não"
        data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
        data5 = f"Prox_concurso: {r['dataProxConcurso']}"
        print(f'{data}\n{data1}\n{data2}\n{venc}\n{prem}\n{data3}\n{data4}\n{data5}')
        pergunta_sim_nao("Gostaria de continuar?")








def pergunta_sim_nao(menssagem):
    resposta = ""
    while resposta not in ("s", "n"):
        resposta = input(f"\n{menssagem}digite: s ou n\n")
        if resposta not in ("s", "n"):
            print("\nVoçê tem que usar as letras \"s\" ou \"n\"\n")
            pergunta_sim_nao("Se quiser começar ")
        elif resposta == "s":
            resp2 = input("< j > Gostaria de fazer jogo(s) da Mega Sena?\n< r > Gostaria de ver o último resultado?\n< p > Gostaria de pesquisar por número de concurso?\ndigite j, r ou p\n")
            if resp2 not in ("j", "r", "p"):
                print("\nVoçê tem que usar as letras \"j\", \"r\" ou \"p\":")
                pergunta_sim_nao("Para tentar de novo ")
            if resp2 == "j":
                Mega.perg1()
            if resp2 == "r":
                Result.ultimo_resultado()
            if resp2 == "p":
                Result.qual_concurso()
        else:
           print("\n__ Boa sorte!\n >>>>> Até a próxima!!!")
           break





pergunta_sim_nao("~~~~~~ Bem vindo ____\nBora começar!?!?\n")


