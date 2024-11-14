def hanoi_first(n, p_from, p_to):
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    hanoi_first(n - 1, p_from, 1 + 2 + 3 - p_to - p_from)
    print(n, p_from, p_to)  # put largest
    hanoi_first(n - 1, 1 + 2 + 3 - p_to - p_from, p_to)


def hanoi(n, p_from):
    # if p_from == 1:

    # with open("output.txt", 'w') as my_file:
    #     print(my_file.read())
    if n % 2 == 0:
        hanoi_first(n - 1, p_from, 2)
        print(n, p_from, 3)
        hanoi_first(n - 2, 2, 3)
    else:
        hanoi_first(n - 1, p_from, 3)
        # free(2)
        print(n, p_from, 2)
        hanoi_first(n - 2, 3, 2)
    if n % 2 == 0 and n > 2:
        print(1, 3, 2)


# def hanoi(n, p_from):
#     if p_from == 1:
#         if n % 2 == 0:
#             hanoi_first(n - 1, p_from, 2)
#             print(n, p_from, 3)
#             hanoi_first(n - 2, 2, 3)
#         else:
#             hanoi_first(n - 1, p_from, 3)
#             # free(2)
#             print(n, p_from, 2)
#             hanoi_first(n - 2, 3, 2)
#     else:
#         if n % 2 == 0:
#             hanoi_first(n - 1, p_from, 6 - p_from - 3)
#             print(n, p_from, 3)
#             hanoi_first(n - 2, 6 - p_from - 3, 3)
#         else:
#             hanoi_first(n - 1, p_from, 6 - p_from - 2)
#             # free(2)
#             print(n, p_from, 2)
#             hanoi_first(n - 2, 6 - p_from - 2, 2)


hanoi(4, 1)

'''1 1 2
2 1 3
1 2 3
3 1 2
1 3 1
2 3 2
1 1 2
4 1 3
1 2 1
2 2 3
1 1 3'''
