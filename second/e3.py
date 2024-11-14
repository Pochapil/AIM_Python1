def hanoi(n, p_from):
    if p_from == 1:
        if n == 1:
            print(1, 1, 2)
            return
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 1, 2)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 2)
            hanoi(n - 1, 3)
    if p_from == 2:
        if n == 1:
            return
        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, 2, 3)
            hanoi(n - 1, 1)
        else:
            hanoi(n - 1, p_from)
    else:
        if n == 1:
            print(1, 3, 2)
            return
        if n % 2 == 0:
            hanoi(n - 1, p_from)
        else:
            hanoi(n - 1, p_from)
            print(n, 3, 2)
            hanoi(n - 1, 1)


hanoi(3, 1)
