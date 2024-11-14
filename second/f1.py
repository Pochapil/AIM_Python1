def hanoi(n, p_from, p_to):
    if n == 1:
        print(1, p_from, p_to)
        return
    free_and_build()
    swap(p_from, p_to)

    def swap(p_from, p_to):
        ...

    hanoi(n, p_from, p_to)


def free_and_build(n, p_from, p_to):
    if n == 0:
        print(1, p_from, p_to)
