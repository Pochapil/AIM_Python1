def hanoi(n, p_from, p_to):
    ...
    # if p_from != 2 and p_to != 2:
    #     if n == 1:
    #         print(1, p_from, 2)
    #         print(1, 2, p_to)
    #         return
    #     hanoi(n - 1, p_from, p_to)
    #     print(n, p_from, 2)
    #     hanoi(n - 1, p_to, p_from)
    #     print(n, 2, p_to)
    #     hanoi(n - 1, p_from, p_to)
    # else:
    #     if n == 1:
    #         print(1, p_from, p_to)
    #         return
    #     hanoi(n - 1, p_from, p_to)
    #     print(n, p_from, 2)
    #     hanoi(n - 1, p_to, p_from)
    #     print(n, 2, p_to)
#     #     hanoi(n - 1, p_from, p_to)
#
#     if n == 1:
#         if p_from == 2 or p_to == 2:
#
#
#
#         if p_from != 2 and p_to != 2:
#             print(1, p_from, 1 + 2 + 3 - p_to - p_from)
#             print(1, 1 + 2 + 3 - p_to - p_from, p_to)
#             return
#         else:
#             print(1, p_from, p_to)
#             return
#     hanoi(n - 1, p_from, p_to)
#     print(n, p_from, 1 + 2 + 3 - p_to - p_from)
#     hanoi(n - 1, p_to, p_from)
#     print(n, 1 + 2 + 3 - p_to - p_from, p_to)
#     hanoi(n - 1, p_from, p_to)
#
#
# hanoi(2, 2, 3)

# def move(n, p_from, p_to):
#     hanoi(n - 1, p_from, p_to)
#     move(n - 1, p_from, p_to)
#
#     # move(n - 1, p_from, 1 + 2 + 3 - p_to)
#     #
#     # hanoi(1, p_to, p_from)
#     # move(n - 1, 1 + 2 + 3 - p_to, p_to)
#
#     if p_from == 2 or p_to == 2:
#         print(1, p_from, p_to)
#     else:
#         ...
#
#
# if n == 2:
#     ...
#
# if (p_from == 3 and p_to == 1) or (p_from == 1 and p_to == 3):
#     print()
#     pass
#
# hanoi(n - 1, p_from, 1 + 2 + 3 - p_to - p_from)
# print(n, p_from, p_to)  # put largest
# hanoi(n - 1, 1 + 2 + 3 - p_to - p_from, p_to)
