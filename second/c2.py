def hanoi(n, p_from, p_to):
    if (p_from == 1 and p_to == 2) or (p_from == 2 and p_to == 3) or (p_from == 3 and p_to == 1):
        if n == 1:
            print(1, p_from, p_to)
            return
        hanoi(n - 1, p_from, p_to)
        hanoi(n - 1, p_to, 6 - p_from - p_to)
        print(n, p_from, p_to)
        hanoi(n - 1, 6 - p_from - p_to, p_from)
        hanoi(n - 1, p_from, p_to)
    else:
        if n == 1:
            print(1, p_from, 6 - p_from - p_to)
            print(1, 6 - p_from - p_to, p_to)
            return
        hanoi(n - 1, p_from, 6 - p_from - p_to)
        hanoi(n - 1, 6 - p_from - p_to, p_to)
        print(n, p_from, 6 - p_from - p_to)
        hanoi(n - 1, p_to, p_from)
        print(n, 6 - p_from - p_to, p_to)
        hanoi(n - 1, p_from, 6 - p_from - p_to)
        hanoi(n - 1, 6 - p_from - p_to, p_to)


hanoi(2, 1, 3)
