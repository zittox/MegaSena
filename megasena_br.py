
# MEGA SENA ____  Gerador aleatório de jogos
# por: github.com/zittox
# colaborador: github.com/ozzysp
# api de resultados: github.com/guto-alves/loterias-api


import time
import qrandom
import requests
from rich import print as rpri
from rich.progress import track
from rich.console import Console
from rich.table import Table

console = Console()





class Mega:

    def perg1():
        while True:
            quantinum = console.input("[bold white on blue]\nQuantos números tem o jogo da MEGA SENA que você quer?[/]\n[bold italic red]digite uma opção: 6, 7, 8 ou 9\n")
            try:
                quantinum = int(quantinum)
                if 6 <= quantinum <= 9:
                    rpri(f"[bold white on blue]\n~~~~>> Você escolheu ter {quantinum} números em cada jogo ----~!~~!~~!\n")
                    break
                else:
                    rpri("\n[bold italic green on red blink]!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!")
                    Mega.perg1()
            except ValueError:
                rpri("\n[bold italic green on red blink]!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                Mega.perg1()
            return quantinum

        def perg2():

            while True:
                numjog = console.input(f"[bold white on blue]Quantos jogos você gostaria de ter com {quantinum} números?\n")
                try:
                    numjog = int(numjog)
                    if numjog == 0:
                        rpri("\n[bold italic green on red blink]!!!!! >>>> ZERO jogadas não é um número válido neh, tenta de novo! <<<< !!!!\n")
                        perg2()
                    if numjog > 100:
                        rpri("\n[bold italic green on red blink]O máximo são 100 jogadas <<<--------\n")
                        perg2()
                    elif numjog >= 1 and numjog <= 100:
                        rpri(f"[bold white on blue]\n~~~~>> Você escolheu {numjog} jogos\n")
                    break
                except ValueError:
                    rpri("\n[bold italic green on red blink]!!!!! >>>> PRESTENÇÃO: digite um número entre 1 e 100 <<<< !!!!\n")
                    perg2()
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
                    console.print(f'[bold white on blue]O jogo de {quantinum} número é :\n{jogox2}', overflow="fold", style="bold")
                    pergunta_sim_nao("Gostaria de continuar?\n")
                else:
                    console.print(f'[bold white on blue]Os {numjog} jogos de {quantinum} números são:\n\nCALCULANDO:', overflow="fold", style="bold")

                    for _ in track(range(numjog), description="", style="cornflower_blue"):
                        time.sleep(0.1)
                    console.print(f'\n{jogox2}\n', overflow="fold", style="bold")
                    pergunta_sim_nao("Gostaria de continuar?\n")
            mostra_jogo()
        perg2()


class Result:

    def ultimo_resultado():

        apicaixa ='https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest'
        r = requests.get(apicaixa).json()
        data = f"Concurso: {r['concurso']}"
        data1 = f"Data: {r['data']}"
        data2 = f"Dezenas: {r['dezenas']}"
        if r['premiacoes'][0]['vencedores'] == 0:
            venc = f"Vencedores: Não"
        else:
            d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
            venc = f"Vencedores: {r['premiacoes'][0]['vencedores']} - {d}"
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
        console.print(f'[blue1]{data}[/]\n[light_slate_blue]{data1}[/]\n[chartreuse3]{data2}[/]\n[yellow2]{venc}[/]\n[red3]{prem}[/]\n[light_slate_blue]{data3}[/]\n[red3]{data4}[/]\n[light_slate_blue]{data5}[/]')
        pergunta_sim_nao("Gostaria de continuar? ")

    def qual_concurso():
        conc = console.input("[bold white on blue]Digite o número do concurso que deseja pesquisar:\n")
        apicaixaconc = f'https://loteriascaixa-api.herokuapp.com/api/mega-sena/{conc}'
        if conc.isnumeric():

            try:
                r = requests.get(apicaixaconc).json()
                data = f"Concurso: {r['concurso']}"
                data1 = f"Data: {r['data']}"
                data2 = f"Dezenas: {r['dezenas']}"
                if r['premiacoes'][0]['vencedores'] == 0:
                    venc = f"Vencedores: Não"
                else:
                    d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
                    venc = f"Vencedores: {r['premiacoes'][0]['vencedores']} - {d}"
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
                console.print(f'[blue1]{data}[/]\n[light_slate_blue]{data1}[/]\n[chartreuse3]{data2}[/]\n[yellow2]{venc}[/]\n[red3]{prem}[/]\n[light_slate_blue]{data3}[/]\n[red3]{data4}[/]\n[light_slate_blue]{data5}[/]')
                pergunta_sim_nao("Gostaria de continuar? ")
            except ValueError:
                console.print(f"[bold italic green on red blink]Concurso não encontrado!\n")

                pergunta_sim_nao("Para tentar de novo ")
        else:
            console.print(f"[bold italic green on red blink]Você não digitou número, digite números válidos!\n")

            pergunta_sim_nao("Para tentar de novo ")
                







def pergunta_sim_nao(menssagem):
    resposta = ""
    while resposta not in ("s", "n"):
        resposta = console.input(f"[bold white on blue]\n{menssagem}digite: s ou n\n")
        if resposta not in ("s", "n"):
            console.print("\n[bold italic green on red blink]Voçê tem que usar as letras \"s\" ou \"n\"\n")
            pergunta_sim_nao("Tenta de novo? ")
        elif resposta == "s":

            table = Table(title=' ', style="deep_sky_blue1")
            table.add_column("Opções", style="green1", no_wrap=True)
            table.add_column("Funções", style="turquoise2", no_wrap=True)
            table.add_row(" J ", "Fazer jogo(s) da Mega Sena")
            table.add_row(" R ", "Ver o resultado do último concurso")
            table.add_row(" P ", "Pesquisar por número de concurso")
            console.print(table)
            resp2 = console.input("[bold white on blue]\nDigite a opção desejada:\n")

            if resp2 not in ("j", "r", "p"):
                console.print("[bold italic green on red blink]\nVoçê tem que usar as letras \"j\", \"r\" ou \"p\":")
                pergunta_sim_nao("Tenta de novo? ")
            if resp2 == "j":
                Mega.perg1()
            if resp2 == "r":
                Result.ultimo_resultado()
            if resp2 == "p":
                Result.qual_concurso()

        else:
            console.print("[bold green on black]\n__ Boa sorte!\n >>>>> Até a próxima!!!\n\n")
            exit()






pergunta_sim_nao('\n\n~~~~~~ Bem vindo __________\nBora começa?!?!?\n')


