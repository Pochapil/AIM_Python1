def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def move_single_element(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put_from_bottom(n - 1, 6 - p_from - p_to, p_to)
    hanoi(n - 3, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)
    move_single_element(n - 1, p_from, p_to)


def hanoi(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put_from_bottom(n, p_from, p_to)
    move_single_element(n - 1, p_from, p_to)


def put_from_bottom(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    if n == 2:
        put_from_bottom(n - 1, p_from, p_to)
        swap(p_from, p_to)
    if n == 3:
        put_from_bottom(n - 1, p_from, p_to)
        print(1, p_from, 6 - p_from - p_to)
        swap(p_from, p_to)
    if n >= 4:
        put_from_bottom(n - 1, p_from, p_to)
        hanoi(n - 4, 6 - p_from - p_to, p_to)
        swap(p_from, 6 - p_from - p_to)
        move_single_element(n - 3, p_from, 6 - p_from - p_to)
        swap(p_from, p_to)
