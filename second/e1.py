def hanoi(n, p_from):
    # if n == 1:
    #     if p_from == 2:
    #         print(1, p_from, 3)
    #     if p_from == 3:
    #         print(1, p_from, 1)
    #     else:
    #         print(1, p_from, 2)
    #     return
    if n == 1:
        if p_from != 2:
            print(1, p_from, 2)
        else:
            print(1, p_from, 6 - p_from - 2)
        return
        # return
    if p_from == 1:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 2)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 2)
            hanoi(n - 1, 3)
    elif p_from == 2:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 1)
        else:
            hanoi(n - 1, p_from)
    else:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 1)


hanoi(4, 1)
