print("""The program will let you play the well-known game Tic-Tac-Toe.
To start a game insert 'start'
To replay the game insert 'restart'
To end the program insert 'stop'""")



pr_state = input("> ")
while pr_state != "start" and pr_state != "restart" and pr_state != "stop" and pr_state != "lol":
    print("""To start a game insert 'start'
    To replay the game insert 'restart'
    To end the program insert 'stop'""")
    pr_state = input("> ")
    print(pr_state)

# ggE retsaE loooooooool
if pr_state == "lol":
    print("""   ,
_,,)\.~,,._
(()`  ``)\))),,_
 |     \ ''((\)))),,_          ____
 |6`   |   ''((\())) \"-.____.-\"    `-.-,
 |    .'\    ''))))'                 \)))
 |   |   `.     ''                    ((((
 \, _)     \/                         |))))
  `'        |                         (((((
            \                  |      ))))))
             `|   |           ,\    /((((((
              |   / `-._____.<  \  |  )))))
              |   |  /        `. \ \  ((((
              |  / \ |          `.\ | (((
              \  | | |             )| | ))
               | | | |             || | '""")
    ok = 0
    while ok < 500:
        print("               | | | |             || |")
        ok += 1
        

while pr_state == "start" or pr_state == "restart":
    if pr_state == "restart":
        print("Well, another game!")
    print("---------")
    print("|       |")
    print("|       |")
    print("|       |")
    print("---------")
    input_str_list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    count = 0
    while True:
        # Stage 4 /X/
        while True:
            # horizontal lists
            H = [[input_str_list[0]], [input_str_list[1]], [input_str_list[2]]]
            H1 = [H[0]]
            H2 = [H[1]]
            H3 = [H[2]]

            # vertical lists
            V = [[input_str_list[0][0], input_str_list[1][0], input_str_list[2][0]], [input_str_list[0][1], input_str_list[1][1], input_str_list[2][1]], [input_str_list[0][2], input_str_list[1][2], input_str_list[2][2]]]
            V1 = V[0]
            V2 = V[1]
            V3 = V[2]

            # diagonal lists
            D = [[input_str_list[0][0], input_str_list[1][1], input_str_list[2][2]], [input_str_list[0][2], input_str_list[1][1], input_str_list[2][0]]]
            D1 = D[0]
            D2 = D[1]

            move = input("Enter the coordinates: >")
            movelist = move.split()
            check = 0
            # move should be integer
            while True:
                if movelist[0].isnumeric() and movelist[1].isnumeric():
                    check += 1
                    break
                else:
                    print("You should enter numbers!")
                    move = input("Enter the coordinates: >")
                    movelist = move.split()

            # move should be of the right index
            while True:
                if int(movelist[0]) > 3 or int(movelist[1]) > 3:
                    print("Coordinates should be from 1 to 3!")
                    move = input("Enter the coordinates: >")
                    movelist = move.split()
                else:
                    check += 1
                    break

            while True:
                movelist = move.split()
                move_y = int(movelist[1])
                move_x = int(movelist[0])
                x = 0
                y = 0

                if move_y == 3:
                    y = 0
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2
                elif move_y == 2:
                    y = 1
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2
                else:
                    y = 2
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2

                if move_y == 3:
                    if H1[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

                if move_y == 2:
                    if H2[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

                if move_y == 1:
                    if H3[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

            if check == 3:
                break
            else:
                check = 0

        if move_y == 3:
            if move_x == 1:
                H1[0][0][0] = "X"
            elif move_x == 2:
                H1[0][0][1] = "X"
            elif move_x == 3:
                H1[0][0][2] = "X"
        if move_y == 2:
            if move_x == 1:
                H2[0][0][0] = "X"
            elif move_x == 2:
                H2[0][0][1] = "X"
            elif move_x == 3:
                H2[0][0][2] = "X"
        if move_y == 1:

            if move_x == 1:
                H3[0][0][0] = "X"
            elif move_x == 2:
                H3[0][0][1] = "X"
            elif move_x == 3:
                H3[0][0][2] = "X"
        print("---------")
        print("|", " ".join(H1[0][0]), "|")
        print("|", " ".join(H2[0][0]), "|")
        print("|", " ".join(H3[0][0]), "|")
        print("---------")

        # horizontal lists
        H = [[input_str_list[0]], [input_str_list[1]], [input_str_list[2]]]
        H1 = [H[0]]
        H2 = [H[1]]
        H3 = [H[2]]

        # vertical lists
        V = [[input_str_list[0][0], input_str_list[1][0], input_str_list[2][0]], [input_str_list[0][1], input_str_list[1][1], input_str_list[2][1]], [input_str_list[0][2], input_str_list[1][2], input_str_list[2][2]]]
        V1 = V[0]
        V2 = V[1]
        V3 = V[2]

        # diagonal lists
        D = [[input_str_list[0][0], input_str_list[1][1], input_str_list[2][2]], [input_str_list[0][2], input_str_list[1][1], input_str_list[2][0]]]
        D1 = D[0]
        D2 = D[1]

        # win conditions / X /

        if H3[0][0] == ["X", "X", "X"] or H2[0][0] == ["X", "X", "X"] or H1[0][0] == ["X", "X", "X"]:
            print("X wins")
            break
        if V1 == ["X", "X", "X"] or V2 == ["X", "X", "X"] or V1 == ["X", "X", "X"]:
            print("X wins")
            break
        if D2 == ["X", "X", "X"] or D1 == ["X", "X", "X"]:
            print("X wins")
            break
        else:
            count += 1

        if count >= 9:
            print("Draw")
            break


        # Stage 4 /O/
        while True:
            # horizontal lists
            H = [[input_str_list[0]], [input_str_list[1]], [input_str_list[2]]]
            H1 = [H[0]]
            H2 = [H[1]]
            H3 = [H[2]]

            # vertical lists
            V = [[input_str_list[0][0], input_str_list[1][0], input_str_list[2][0]], [input_str_list[0][1], input_str_list[1][1], input_str_list[2][1]], [input_str_list[0][2], input_str_list[1][2], input_str_list[2][2]]]
            V1 = V[0]
            V2 = V[1]
            V3 = V[2]

            # diagonal lists
            D = [[input_str_list[0][0], input_str_list[1][1], input_str_list[2][2]], [input_str_list[0][2], input_str_list[1][1], input_str_list[2][0]]]
            D1 = D[0]
            D2 = D[1]
            move = input("Enter the coordinates: >")
            movelist = move.split()
            check = 0
            # move should be integer
            while True:
                if movelist[0].isnumeric() and movelist[1].isnumeric():
                    check += 1
                    break
                else:
                    print("You should enter numbers!")
                    move = input("Enter the coordinates: >")
                    movelist = move.split()

            # move should be of the right index
            while True:
                if int(movelist[0]) > 3 or int(movelist[1]) > 3:
                    print("Coordinates should be from 1 to 3!")
                    move = input("Enter the coordinates: >")
                    movelist = move.split()
                else:
                    check += 1
                    break

            while True:
                movelist = move.split()
                move_y = int(movelist[1])
                move_x = int(movelist[0])
                x = 0
                y = 0

                if move_y == 3:
                    y = 0
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2
                elif move_y == 2:
                    y = 1
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2
                else:
                    y = 2
                    if move_x == 1:
                        x = 0
                    elif move_x == 2:
                        x = 1
                    else:
                        x = 2

                if move_y == 3:
                    if H1[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

                if move_y == 2:
                    if H2[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

                if move_y == 1:
                    if H3[0][0][x] != "_":
                        print("This cell is occupied! Choose another one!")
                        move = input("Enter the coordinates: >")
                    else:
                        check += 1
                        break

            if check == 3:
                break
            else:
                check = 0

        if move_y == 3:
            if move_x == 1:
                H1[0][0][0] = "O"
            elif move_x == 2:
                H1[0][0][1] = "O"
            elif move_x == 3:
                H1[0][0][2] = "O"
        if move_y == 2:
            if move_x == 1:
                H2[0][0][0] = "O"
            elif move_x == 2:
                H2[0][0][1] = "O"
            elif move_x == 3:
                H2[0][0][2] = "O"
        if move_y == 1:

            if move_x == 1:
                H3[0][0][0] = "O"
            elif move_x == 2:
                H3[0][0][1] = "O"
            elif move_x == 3:
                H3[0][0][2] = "O"
        print("---------")
        print("|", " ".join(H1[0][0]), "|")
        print("|", " ".join(H2[0][0]), "|")
        print("|", " ".join(H3[0][0]), "|")
        print("---------")

        # horizontal lists
        H = [[input_str_list[0]], [input_str_list[1]], [input_str_list[2]]]
        H1 = [H[0]]
        H2 = [H[1]]
        H3 = [H[2]]

        # vertical lists
        V = [[input_str_list[0][0], input_str_list[1][0], input_str_list[2][0]], [input_str_list[0][1], input_str_list[1][1], input_str_list[2][1]], [input_str_list[0][2], input_str_list[1][2], input_str_list[2][2]]]
        V1 = V[0]
        V2 = V[1]
        V3 = V[2]

        # diagonal lists
        D = [[input_str_list[0][0], input_str_list[1][1], input_str_list[2][2]], [input_str_list[0][2], input_str_list[1][1], input_str_list[2][0]]]
        D1 = D[0]
        D2 = D[1]

        # win conditions / O /

        if H3[0][0] == ["O", "O", "O"] or H2[0][0] == ["O", "O", "O"] or H1[0][0] == ["O", "O", "O"]:
            print("O wins")
            break
        if V3 == ["O", "O", "O"] or V2 == ["O", "O", "O"] or V1 == ["O", "O", "O"]:
            print("O wins")
            break
        if D2 == ["O", "O", "O"] or D1 == ["O", "O", "O"]:
            print("O wins")
            break
        else:
            count += 1

    print("Do you want to play again? You know what to do")
    pr_state = input("> ")

if pr_state == "stop":
    print("""Hope you enjoied!
Bye!!""")


# The End
# ore 19:07 01/06/2020,località di Iseo. Ho appena terminato e controllato il mio primo programma complesso funzionante. Sono abbastanza felice direi.
# ho lavorato per oltre un mese, e sono state 37 ore di lavoro ben spese

# il programmatore, Marco Volpato
