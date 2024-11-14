def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def put(n, p_from, p_to, flag):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, p_from, p_to, flag)
    build(n - 2, p_from, 6 - p_from - p_to, flag)
    swap(p_from, p_to)



def build(n, p_from, p_to, flag):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    hanoi(n, p_from, p_to, flag)


def hanoi(n, p_from, p_to, flag=True):
    # flag - if first entry

    if n == 1:
        print(1, p_from, p_to)
        return
    if flag:
        put(n, p_from, p_to, flag)
        # put(n - 1, p_from, p_to)  # 3
        # build(n - 2, p_from, 6 - p_from - p_to)  # 2
        # swap(p_from, p_to)
    else:
        put(n - 1, 2, 3, flag)  # 3
        build(n - 2, 1, 2, flag)  # 2
        swap(p_from, p_to)

    flag = False
    hanoi(n - 1, p_from, p_to, flag)


hanoi(4, 1, 3)


'''1 1 3
0 1 3
1 1 2
0 1 3
1 1 2
0 1 2
1 3 2
0 1 3
1 2 3
0 2 3
0 1 3
1 2 3
0 1 3
1 1 3'''


def free_and_build(n, p_from, p_to):
    if n == 0:
        print(1, p_from, p_to)
