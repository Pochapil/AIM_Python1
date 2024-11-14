def hanoi(n, p_from):
    if p_from == 1:
        if n == 1:
            print(1, 1, 2)
            return
        if n == 2:
            hanoi(n - 1, p_from)
            print(2, 1, 3)

    if p_from == 2:
        if n == 1:
            print(1)
