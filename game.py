import random
import math
from inputimeout import inputimeout


def logic(p_name, t, score_p, score_cpu, k):

    # ----------------------------------------------- READING DATA FROM FILE --------------------------------------------#

    my_file = open("places.txt", "r", encoding="utf-8")
    temp = (
        my_file.read()
    )  # reading for appropriate name of places stored in a plain text.
    conv_list = temp.split()  # converting read data into list.
    upper = (
        temp.upper()
    ).split()  # converting read data into list of uppercase elements
    a = t
    for_alphabet = [  # list containing all the alphabets
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    print("\n")

    # ----------------------------------------------------- MAIN LOGIC ---------------------------------------------------#

    while t > 0:
        t = t - k
        try:
            print(" ")
            print(f"Giving a random letter, to {p_name}........")
            p_got = random.choice(
                for_alphabet
            )  # generating a random letter for player with which he would start the game.
            print(
                f"hey you got '{p_got}',name any place starting with alphabet '{p_got}' "
            )
            p_ans = str(
                inputimeout(prompt="your choice- ", timeout=5)
            )  # used inputimeout module to set time limit in user's answer.
            ans_end = p_ans[-1]
            filtering = [i for i in conv_list if i[0].lower() == ans_end.lower()]

            if (
                p_ans in conv_list
                and p_ans.startswith(p_got)
                or p_ans in upper
                and p_ans.startswith(p_got)
            ):
                cpu_got = random.choice(filtering).upper()
                print("cpu_choose- ", cpu_got)
                score_p = score_p + 1
                score_cpu += 1
                my_file.close()
            else:
                print(
                    "SORRY, THERE IS SOMETHING WRONG WITH YOUR ANSWER (CHANCE SKIPPED) :("
                )  # marks as wrong input if not matched with the data in list.
                cpu_got = random.choice(filtering)
                score_cpu += 1
                print("cpu_choose- ", cpu_got)
                print(" ")
        except BaseException as e:
            print("\n")
            print(
                "GAME-OVER BECAUSE U EXCEEDED THE TIME LIMIT -_- ", e
            )  # skipping of chance if player exceeds the time limit.
            exit()

    # ---------------------------------------------------- FINDING EFFICIENCY --------------------------------------------------#

    print("\n")
    eff = float((score_p / a) * 100)
    efficiency = round(eff, 2)
    if efficiency == 100:
        print(f"Hurray {p_name} u won all the rounds and were 100% efficient :O ")
    else:
        if efficiency < 100 and efficiency >= 80:
            print(f"{p_name}, YOU WERE {efficiency}% efficient, NICE TRY :) ")
        elif efficiency < 80 and efficiency >= 65:
            print(
                f"{p_name}, YOU WERE {efficiency}% efficient, YOU CAN DO MUCH BETTER! "
            )
        else:
            print(f"{p_name}, YOU WERE {efficiency}% efficient, TRY TO IMPROVE :(")
        print(" ")
    return "-----------------<<< KEEP EXPLORING >>>-------------------"


# ------------------------------------------------------------------------------------------------------------------------------#

p_name = input("Enter your name ")
t = int(input("Enter no of rounds to play "))
print(logic(p_name, t, 0, 0, 1))
