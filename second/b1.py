def hanoi(n, p_from, p_to):
    if p_from == 2 or p_to == 2:
        if n == 1:
            print(1, p_from, p_to)
            return
        hanoi(n - 1, p_from, 1 + 2 + 3 - p_to - p_from)
        print(n, p_from, p_to)
        hanoi(n - 1, 1 + 2 + 3 - p_to - p_from, p_to)
    else:
        if n == 1:
            print(1, p_from, 1 + 2 + 3 - p_to - p_from)
            print(1, 1 + 2 + 3 - p_to - p_from, p_to)
            return
        hanoi(n - 1, p_from, p_to)
        print(n, p_from, 1 + 2 + 3 - p_to - p_from)
        hanoi(n - 1, p_to, p_from)
        print(n, 1 + 2 + 3 - p_to - p_from, p_to)
        hanoi(n - 1, p_from, p_to)


hanoi(2, 1, 3)
