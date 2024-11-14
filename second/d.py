def hanoi(n, p_from, p_to):
    if n == 1:
        print(1, p_from, p_to)
        return
    if p_from == 2:
        hanoi(n - 1, p_from, 6 - p_from - p_to)
        print(n, p_from, p_to)
        hanoi(n - 1, 6 - p_from - p_to, p_to)
    else:
        hanoi(n - 1, p_from, p_to)
        print(n, p_from, 2)
        hanoi(n - 1, p_to, p_from)
        print(n, 2, p_to)
        hanoi(n - 1, p_from, p_to)

hanoi(2, 1, 3)