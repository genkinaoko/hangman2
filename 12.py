def hangman(word):
    wrong = 0
    stages =["", 
             "______      ",
             "|           ",
             "|     |     ",
             "|     O     ",
             "|    /|\    ",
             "|    / \    ",
             "|           "
             ]
    letter = list(word)
    board = ["_"] * len(word)
    win = False
    print("Wellcome to hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Please type one word!")
        if char in letter:
            id = letter.index(char)
            board[id] = char
            letter[id] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You WIN !")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! Answer is {}.".format(word))

hangman("hamburger")
