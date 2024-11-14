def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def put(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, p_from, p_to)
    hanoi(n - 2, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)
    return

def hanoi(n, p_from, p_to):
    # flag - if first entry
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, p_from, p_to)  # 3
    hanoi(n - 2, p_from, 6 - p_from - p_to)  # 2
    swap(p_from, p_to)
    hanoi(n - 1, 6 - p_from - p_to, p_to)


hanoi(3, 1, 3)
