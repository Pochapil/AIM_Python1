def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def hanoi(n, p_from, p_to, flag=True):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    # if flag:
    put(n, p_from, p_to)
    # flag = False
    put(n - 2, 6 - p_from - p_to, p_to)
    hanoi(n - 4, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)
    hanoi(n - 1, p_from, p_to)


def put(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, p_from, p_to)
    hanoi(n - 4, 6 - p_from - p_to, p_to)
    free(n - 2, p_from, p_to)
    swap(p_from, p_to)


def free(n, p_from, p_to):
    if n == 0:
        return
    if n == 1:
        print(n, p_from, 6 - p_from - p_to)
        return
    # hanoi(n - 2, 6 - p_from - p_to, p_to)
    swap(p_from, 6 - p_from - p_to)
    put(n - 2, p_to, 6 - p_from - p_to)
    hanoi(n - 3, p_from, p_to)
    free(n - 1, p_from, p_to)


hanoi(2, 1, 3)
