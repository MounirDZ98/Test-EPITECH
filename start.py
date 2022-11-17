def start(L):

    for i in range(1,L+2) :

        if i <= L:
            for j in range(1, 3 * L - i + 1):
                print(" ", end="")
            for j in range(1, 2 * i - 1 + 1):
                if j == 1 or j == 2 * i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

        elif i == L + 1:
            for j in range(1, 6 * L - 1 + 1):
                if (j >= 1 and j <= 2 * L + 1) or (j >= 4 * L - 1 and j <= 6 * L):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    for i in range(1, 2 * L - 1 + 1):
        if i <= L:
            for j in range(1, i + 1):
                print(" ", end="")
        else:
            for j in range(1, 2 * L - i + 1):
                print(" ", end="")
        for j in range(1, L + 1):
            if j == 1:
                print("*", end="")
        if i <= L:
            for j in range(1, L - i + 1):
                print(" ", end="")
        else:
            for j in range(1, i - L + 1):
                print(" ", end="")
        for j in range(1, 4 * L - 3 + 1):
            print(" ", end="")

        if i <= L:
            for j in range(1, L - i +1):
                print(" ", end="")
        else:
            for j in range(1, i - L + 1):
                print(" ", end="")
        for j in range(1, L + 1):
            if j == 1:
                print("*", end="")
        print()

    for i in range(1, L + 1 + 1):
        if i == 1:
            for j in range(1, 6 * L - 1 + 1):
                if (j >= 1 and j <= 2 * L + 1) or (j >= 4 * L - 1 and j <= 6 * L):
                    print("*", end="")
                else:
                    print(" ", end="")
        else:
            for j in range(1, 2 * L + i - 2 + 1):
                print(" ", end="")
            for j in range(1, L - i + 2 + 1):
                if j == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            for j in range(1, L - i + 1):
                print(" ", end="")
            for j in range(1, L - i + 2):
                if j == 1:
                    print("*", end="")
        print()

L = int(input("Veuillez saisir le nombre de lignes : "));
start(L);










