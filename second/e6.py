def hanoi(n, p_from):
    if n <= 0:
        return

    # if n == 2:
    #     if p_from == 1:
    #         hanoi(n - 1, p_from)
    #         print(2, p_from, 3)
    #     elif p_from == 2:
    #         hanoi(n - 1, p_from)
    #         print(2, p_from, 3)
    #     else:
    #         hanoi(n - 1, p_from)
    #     return
    if n == 1:
        if p_from == 1:
            print(1, p_from, 2)
        elif p_from == 2:
            print(1, p_from, 3)
        else:
            print(1, p_from, 2)
        return

    if p_from == 1:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 2, 2)
        else:
            hanoi(n - 1, p_from)
            if n == 3:
                hanoi(n - 2, 2)
            print(n, p_from, 2)
            hanoi(n - 2, 3)
    else:
        hanoi(n - 1, 6 - p_from - 1)


hanoi(4, 1)
