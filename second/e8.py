def hanoi_first(n, p_from, p_to, my_file):
    if n <= 0:
        return
    if n == 1:
        my_file.write(f'1 {p_from} {p_to}\n')
        return
    hanoi_first(n - 1, p_from, 1 + 2 + 3 - p_to - p_from, my_file)
    my_file.write(f'{n} {p_from} {p_to}\n')  # put largest
    hanoi_first(n - 1, 1 + 2 + 3 - p_to - p_from, p_to, my_file)


def hanoi(n, p_from):
    with open("output.txt", 'w') as my_file:
        if n % 2 == 0:
            hanoi_first(n - 1, p_from, 2, my_file)
            my_file.write(f'{n} {p_from} {3}\n')
            hanoi_first(n - 2, 2, 3, my_file)
        else:
            hanoi_first(n - 1, p_from, 3, my_file)
            my_file.write(f'{n} {p_from} {2}\n')
            hanoi_first(n - 2, 3, 2, my_file)
    if n > 2:
        flag = False
        with open('output.txt', 'r') as fh:
            for line in fh:
                pass
            last_line = line
            if last_line[-2] != '2':
                flag = True
        if flag:
            with open("output.txt", 'a') as my_file:
                my_file.write(f'{1} {3} {2}\n')
    # with open('output.txt', 'rb+') as fh:
    #     fh.seek(-2, 2)
    #     fh.truncate()

hanoi(2, 1)
