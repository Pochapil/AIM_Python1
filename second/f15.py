def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def recursion_func(n, p_from, p_to):
    if n <= 0:
        return
    put(n, 6 - p_from - p_to, p_to)
    hanoi(n - 2, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)

    recursion_func(n - 1, p_from, p_to)


def hanoi(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n, p_from, p_to)

    recursion_func(n - 2, p_from, p_to)
    # put(n - 2, 6 - p_from - p_to, p_to)
    # hanoi(n - 4, p_from, 6 - p_from - p_to)
    # swap(p_from, p_to)
    #
    # put(n - 3, 6 - p_from - p_to, p_to)
    # hanoi(n - 5, p_from, 6 - p_from - p_to)
    # swap(p_from, p_to)

    put(1, p_from, p_to)


def rec(n, p_from, p_to):
    if n <= 1:
        return
    put(n, p_to, 6 - p_from - p_to)
    hanoi(n, p_from, p_to)
    swap(p_from, 6 - p_from - p_to)

    rec(n - 1, p_from, p_to)


def put_rec(n, p_from, p_to):
    if n == 1:
        print(1, p_from, p_to)
        return

    if n == 4:
        put_rec(n - 1, p_from, p_to)
        # print(1, p_from, 6 - p_from - p_to)
        swap(p_from, 6 - p_from - p_to)
        print(1, p_from, 6 - p_from - p_to)
        swap(p_from, p_to)
    if n == 3:
        put_rec(n - 1, p_from, p_to)
        print(1, p_from, 6 - p_from - p_to)
        swap(p_from, p_to)
    if n == 2:
        put_rec(n - 1, p_from, p_to)
        swap(p_from, p_to)
        # print(1, p_from, 6 - p_from - p_to)

    if n > 4:
        put_rec(n - 1, p_from, p_to)
        hanoi(n - 4, 6 - p_from - p_to, p_to)
        swap(p_from, 6 - p_from - p_to)
        rec(n - 4, p_from, p_to)
        swap(p_from, p_to)

    # rec(n - 4)
    # put(n - 4, p_to, 6 - p_from - p_to)
    # hanoi(n - 6, p_from, p_to)
    # swap(p_from, 6 - p_from - p_to)

    # -----было
    # hanoi(n - 4, 6 - p_from - p_to, p_to)
    # swap(p_from, 6 - p_from - p_to)
    # rec(n - 4, p_from, p_to)
    # swap(p_from, p_to)
    # ----------

    # put(n - 1, p_from, p_to)
    # hanoi(n - 2, p_from, 6 - p_from - p_to)
    # swap(p_from, p_to)


def put(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return

    put_rec(n, p_from, p_to)

    # put(n - 1, p_from, p_to)
    #
    # swap(p_from, p_to)
    #
    # hanoi(n - 4, 6 - p_from - p_to, p_to)
    # swap(p_from, 6 - p_from - p_to)
    #
    # put(n - 4, p_to, 6 - p_from - p_to)

# hanoi(4, 1, 3)
# put(4, 1, 3)
