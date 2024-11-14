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
    build(n - 2, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)
    return


def build(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n, p_from, p_to)
    build(n - 1, 6 - p_from - p_to, p_to)
    return


def hanoi(n, p_from, p_to, flag=True):
    # flag - if first entry

    if n == 1:
        print(1, p_from, p_to)
        return
    if flag:
        put(n, p_from, p_to)
        # put(n - 1, p_from, p_to)  # 3
        # build(n - 2, p_from, 6 - p_from - p_to)  # 2
        # swap(p_from, p_to)
    else:
        put(n - 1, 2, 3)  # 3
        build(n - 3, 1, 2)  # 2
        swap(p_from, p_to)

    flag = False
    hanoi(n - 1, p_from, p_to, flag)


hanoi(4, 1, 3)


def free_and_build(n, p_from, p_to):
    if n == 0:
        print(1, p_from, p_to)
