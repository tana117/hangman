import random

answers = ["dog", "bird", "elephant", "penguin", "hippopotamus"]
random_answer = random.choice(answers)
print(random_answer)

def hangman(random_answer):
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    / \    ",
              "|           "
              ]
    rletters = list(random_answer)
    board = ["_"] * len(random_answer)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(random_answer))

hangman(random_answer)
