def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def move_left(n, p_from, p_to, flag):
    if not flag:
        if n <= 1:
            return
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, 6 - p_from - p_to, p_to, False)
    # hanoi(n - 3, 6 - p_from - p_to, p_from)
    hanoi(n - 3, p_from, 6 - p_from - p_to, False)
    swap(p_from, p_to)
    move_left(n - 1, p_from, p_to, flag)
    return


def put(n, p_from, p_to, flag):
    
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    # flag = False
    put(n - 1, p_from, p_to, flag)
    hanoi(n - 2, p_from, 6 - p_from - p_to, flag)
    swap(p_from, p_to)

    return


def hanoi(n, p_from, p_to, flag=True):
    # flag - if first entry
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    if flag:
        put(n, p_from, p_to, flag)
        move_left(n - 1, p_from, p_to, flag)
    # hanoi(n -1, p_from, p_to)
    # else:
    # put(n, p_from, p_to)
    return


hanoi(3, 1, 3)
