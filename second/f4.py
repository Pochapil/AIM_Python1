def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def build(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    hanoi(n, p_from, p_to)
    hanoi(n - 2, 6 - p_from - p_to, p_to)
    build(n - 3, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)


def hanoi(n, p_from, p_to, flag=True):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    hanoi(n - 1, p_from, p_to)
    build(n - 2, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)


hanoi(3, 1, 3)

'''1 1 3
0 1 3
1 1 2
0 1 3
1 2 3
0 1 3
1 1 3'''
