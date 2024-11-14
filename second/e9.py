def hanoi_first(n, p_from, p_to):
    if p_from != p_to:
        if n <= 0:
            return
        if n == 1:
            print(1, p_from, p_to)
            return
        hanoi_first(n - 1, p_from, 1 + 2 + 3 - p_to - p_from)
        print(n, p_from, p_to)  # put largest
        hanoi_first(n - 1, 1 + 2 + 3 - p_to - p_from, p_to)
    else:
        return


def hanoi(n, p_from):
    if n <= 0:
        return
    if n % 2 == 0:
        hanoi_first(n - 1, p_from, 2)
        if p_from != 3:
            print(n, p_from, 3)
        hanoi_first(n - 2, 2, 3)
        hanoi(n - 2, 3)
    else:
        hanoi_first(n - 1, p_from, 3)
        if p_from != 2:
            print(n, p_from, 2)
        hanoi_first(n - 2, 3, 2)
        hanoi(n - 2, 2)


hanoi(3, 1)
