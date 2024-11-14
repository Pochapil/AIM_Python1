def hanoi(n, p_from, p_to):
    put(n - 1, p_from, p_to)
    hanoi(n - 4, 6 - p_from - p_to, p_to)
    swap(1, 2)
    # func
    func(n - 4)
    swap(1, 3)

    put(n - 2, 2, 3)
    hanoi(n - 4, 1, 2)
    swap(1, 3)

    put(n - 3, 2, 3)
    hanoi(n - 5, 1, 2)
    swap(1, 3)

    pass


def func(n):
    put(n, 3, 2)  # hanoi n-5 3, 3
    swap(1, 2)
    func(n - 1)


def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def func3(n, p_from, p_to):
    if n <= 0:
        return
    put(n, 2, 3)
    hanoi1(n - 2, 1, 2)
    swap(1, 3)
    func3(n - 1, p_from, p_to)


def hanoi1(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n, p_from, p_to)

    # 6 - p_from, p_to

    func3(n - 2, p_from, p_to)
    # put(n - 2, 2, 3)
    # hanoi(n - 4, 1, 2)
    # swap(1, 3)
    #
    # put(n - 3, 2, 3)
    # hanoi(n - 5, 1, 2)
    # swap()


def func2(n, p_from, p_to):
    if n <= 0:
        return
    swap(1, 2)
    put(n, 3, 2)
    func2(n - 1, p_from, p_to)


def put(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    put(n - 1, 1, 3)
    put(n - 2, 1, 2)
    hanoi1(n - 4, 2, 3)

    func2(n - 4, p_from, p_to)

    # swap(1,2)
    # put(n-4, 3,2)
    # swap(1,2)
    # put(n-5)

    swap(1, 3)

    # hanoi()
    # put(n-3,1,2)
    # swap()


hanoi1(2, 1, 3)
