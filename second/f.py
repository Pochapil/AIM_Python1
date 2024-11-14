def hanoi(n, p_from, p_to):


    free(n - 1, p_from)
    build(n - 1, p_to)
    swap(p_from, p_to)

    def swap(p_from, p_to):
        ...

    hanoi(n, p_from, p_to)


def free(n, p_from):
    if n == 0:
        print(1, p_from, p_to)
