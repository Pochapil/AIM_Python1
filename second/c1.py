def hanoi(n, p_from, p_to):
    if p_from == 1:
        must_p_to = 2
    elif p_from == 2:
        must_p_to = 3
    else:
        must_p_to = 1

    if must_p_to != p_to:
        if n == 1:
            print(1, p_from, must_p_to)
            print(1, must_p_to, p_to)
            return
        hanoi(n - 1, p_from, must_p_to)
        hanoi(n - 1, must_p_to, p_to)
        print(n, p_from, must_p_to)
        hanoi(n - 1, p_to, p_from)
        print(n, must_p_to, p_to)
        hanoi(n - 1, p_from, must_p_to)
        hanoi(n - 1, must_p_to, p_to)
    else:
        if n == 1:
            print(1, p_from, p_to)
            return
        hanoi(n - 1, p_from, must_p_to)
        hanoi(n - 1, must_p_to, 1 + 2 + 3 - p_from - p_to)
        print(n, p_from, p_to)
        hanoi(n - 1, 1 + 2 + 3 - p_from - p_to, p_from)
        hanoi(n - 1, p_from, p_to)


hanoi(2, 1, 3)
