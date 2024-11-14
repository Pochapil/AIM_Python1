def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def func3(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, 6 - p_from - p_to, p_to)
        return
    put(n, p_from, p_to)
    hanoi1(n - 2, 6 - p_from - p_to, p_from)
    swap(6 - p_from - p_to, p_to)
    func3(n - 1, p_from, p_to)


def func(n, p_from, p_to):
    put(n - 1, p_from, p_to)
    hanoi(n - 2, p_from, 6 - p_from - p_to)
    swap(p_from, p_to)


def hanoi(n, p_from, p_to):
    put(n - 1, p_from, p_to)
    hanoi(n - 4, 6 - p_from - p_to, p_to)
    swap(p_from, 6 - p_from - p_to)

    put(n - 5, p_to, 6 - p_from - p_to)

    # func
    func(n - 4, p_from, p_to)
    swap(1, 3)

    put(n - 2, 2, 3)
    hanoi(n - 4, 1, 2)
    swap(1, 3)

    put(n - 3, 2, 3)
    hanoi(n - 5, 1, 2)
    swap(1, 3)


def hanoi1(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return

    put(n, p_from, p_to)
    # if n == 2:
    #     print(1, p_from, p_to)
    func3(n - 2, 6 - p_from - p_to, p_to)


def func2(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, 6 - p_from - p_to)
        # print(1, p_to, 6 - p_from - p_to)
        return
    swap(p_from, 6 - p_from - p_to)
    put(n, p_to, 6 - p_from - p_to)
    hanoi1(n - 1, p_from, p_to)
    func2(n - 1, p_from, p_to)


def put(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    # if n ==2:
    #     print(1, p_from, p_to)
    #     return
    put(n - 1, p_from, p_to)

    # hanoi1(n - 4, 6 - p_from - p_to, p_to)

    # put(n - 2, p_from, 6 - p_from - p_to)
    hanoi1(n - 4, 6 - p_from - p_to, p_to)

    func2(n - 2, p_from, p_to)

    swap(p_from, p_to)


def put_one(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return


hanoi1(2, 1, 3)

# put(4, 1, 3)
