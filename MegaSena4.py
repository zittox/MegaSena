# TURNS = input("How many turns do you want to play? ")
# try:
#     TURNS = int(TURNS)
#     if TURNS > 100:
#         print("You can play a maximum of 100 turns.")
#     elif TURNS > 1 and TURNS < 100:
#         print("You have chosen", TURNS, "turns.")
# except ValueError:
#     print("You must enter a number.")

quantinum = 0
def get_quantinum():
    quantinum = input("Quantas jogadas vc quer fazer? ")
    if quantinum.isnumeric():
        quantinum = int(quantinum)
        if quantinum > 100:
            print("Vc pode jogar no máximo 100 jogadas.")
        elif 1 < quantinum < 100:
            print("Vc quer jogar", quantinum, "jogadas.")
    elif quantinum.isalpha():
        print("Vc deve digitar um numero.")
    else:
        print("Digite um número válido.")

    return quantinum

get_quantinum()

