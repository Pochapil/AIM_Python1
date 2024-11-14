a = [1, 2, 3, 4, 5, 6, 9, 11, 10, 13, 0]


def check(a, a_sort, p_prev, p, p_sort, cur_max, res):
    if p == p_sort:
        if a_sort[p_sort] == cur_max:
            res.append(p_prev)
            p_prev = p
            p += 1
            p_sort += 1
            make_sub_arr(a, a_sort, p_prev, p, p_sort, res)
        else:
            while a_sort[p_sort] != cur_max:  # всегда будет < в отсортированном
                p_sort += 1
            check(a, a_sort, p_prev, p, p_sort, cur_max, res)
    else:
        if p > p_sort:
            p_sort = p
            check(a, a_sort, p_prev, p, p_sort, cur_max, res)
        else:
            cur_max = max(cur_max, max(a[p:p_sort + 1]))
            p = p_sort
            check(a, a_sort, p_prev, p, p_sort, cur_max, res)


def make_sub_arr(a, a_sort, p_prev, p, p_sort, res):
    if p == len(a):
        res.append(p - 1)
        return res
    cur_max = a[p]
    while a[p] != a_sort[p_sort]:
        p += 1
        cur_max = max(cur_max, a[p])
    check(a, a_sort, p_prev, p, p_sort, cur_max, res)
    return res


def func(a):
    a_sort = sorted(a)
    p_prev, p, p_sort = 0, 0, 0
    res = []
    ans = make_sub_arr(a, a_sort, p_prev, p, p_sort, res)
    res_arr = [a[ans[0]:ans[1] + 1]]
    for i in range(1, len(ans) - 1):
        res_arr.append(a[ans[i] + 1:ans[i + 1] + 1])
    for arr in res_arr:
        print(arr)
    return res_arr


func(a)

# def func(a, a_sort, p_prev, p, p_sort, res):
#     cur_max = a[p]
#     while a[p] != a_sort[p_sort]:
#         p += 1
#         cur_max = max(cur_max, a[p])
#
#     if p - p_prev == p_sort - p_prev:
#         if a_sort[p_sort] == cur_max:
#             res.append(p_prev)
#             p_prev = p
#             p += 1
#             p_sort += 1
#             func(a, a_sort, p_prev, p, p_sort, res)
#         else:
#             while a_sort[p_sort] != cur_max:
#                 p_sort += 1
#             cur_max = max(cur_max, a[p:p_sort + 1])
#             p = p_sort
#
#             # func(a, a_sort, p_prev, p, p_sort, res)
#
#
#     else:
#         if p - p_prev > p_sort - p_prev:
#             p_sort = p
#             if a_sort[p_sort] == cur_max:
#                 res.append(p_prev)
#                 p_prev = p
#                 p += 1
#                 p_sort += 1
#                 func(a, a_sort, p_prev, p, p_sort, res)
#             else:
#                 pass
#         else:
#             cur_max = max(cur_max, a[p:p_sort + 1])
#             p = p_sort
#             if a_sort[p_sort] == cur_max:
#                 res.append(p_prev)
#                 p_prev = p
#                 p += 1
#                 p_sort += 1
#                 func(a, a_sort, p_prev, p, p_sort, res)
#             else:
#                 pass
#     return res
