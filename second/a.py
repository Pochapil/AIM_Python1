def hanoi(n, p_from, p_to):
    if n == 1:
        print(1, p_from, p_to)
        return
    hanoi(n - 1, p_from, 1 + 2 + 3 - p_to - p_from)  # move to another
    print(n, p_from, p_to)  # put largest
    hanoi(n - 1, 1 + 2 + 3 - p_to - p_from, p_to)  # now solve for n-1 at another


hanoi(2, 1, 3)
