def hanoi(n, p_from):
    if n == 1:
        if p_from != 2:
            print(1, p_from, 2)
        else:
            print(1, )
        return
    if p_from == 1:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 2)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 2)
            hanoi(n - 1, 3)
    else:
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 2)
        hanoi(n - 1, p_from)


hanoi(4, 1)
