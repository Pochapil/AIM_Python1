def hanoi(n, p_from):
    if p_from == 1:
        if n == 2:
            print(1, p_from, 2)
            print(2, p_from, 3)
            return
        if n == 1:
            print(1, p_from, 2)
            return

        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 2, 2)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 2)
            hanoi(n - 2, 3)
    elif p_from == 2:
        if n == 2:
            print(1, p_from, 1)
            print(2, p_from, 3)
            print(1, p_from, 2)
            return
        if n == 1:
            print(1, p_from, 2)
            return

        if n % 2 == 0:
            hanoi(n - 1, p_from)
            print(n, p_from, 3)
            hanoi(n - 2, 1)
        else:
            # print('wtf')
            hanoi(n - 1, p_from)
            print(n, p_from, 1)
            hanoi(n - 2, 2)
    else:
        if n == 2:
            print(1, p_from, 2)
            return
        if n == 1:
            print(1, p_from, 2)
            return

        if n % 2 == 0:
            # print('wtf')
            hanoi(n - 1, p_from)
            print(n, p_from, 1)
            hanoi(n - 2, 2)
        else:
            hanoi(n - 1, p_from)
            print(n, p_from, 2)
            hanoi(n - 2, 1)


hanoi(2, 1)
