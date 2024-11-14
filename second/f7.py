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


def move_left(n, p_from, p_to):
    put(n - 1, 6 - p_from - p_to, p_to)
    hanoi(n - 3, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)


def build(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n, p_from, p_to)
    build(n - 1, 6 - p_from - p_to, p_to)
    return




def hanoi(n, p_from, p_to):
    if n <= 0:
        return

    if n == 1:
        print(1, p_from, p_to)
        return

    put(n, p_from, p_to)
    hanoi(n - 2, 6 - p_from - p_to, p_to)
    move_left(n - 1, p_from, p_to)
    # move_left()

