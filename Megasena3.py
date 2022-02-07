"This program is a simulation of the Megasena lottery"

import random

"This function asks the user for the number of times he/she wants to play the lottery"
def ask_user():
    "This function asks the user for the number of times he/she wants to play the lottery"
    times = int(input("How many times do you want to play the lottery? "))
    while times <= 100:
        if times < 1:
            print("You must play at least one time")
        elif times > 100:
            print("You can't play more than 100 times")
        else:
            return times


"This function generates the numbers of the lottery"
def generate_numbers(times):
    "This function generates the numbers of the lottery"
    numbers = []
    for i in range(times):
        numbers.append(random.randint(1, 60))
    return numbers


ask_user()
generate_numbers(ask_user())

