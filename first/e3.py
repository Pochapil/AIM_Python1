def find_path_sums(tree):
    stack = [tree]
    buf_sum = 0
    while stack:
        cur_node = stack.pop()
        if isinstance(cur_node, tuple):
            val = cur_node[0]
            left = cur_node[1]
            right = cur_node[2]

            buf_sum += val
            if left is None and right is None:
                print(buf_sum)
                buf_sum -= val
            else:
                stack.append(val)
                stack.append(right)
                stack.append(left)
        else:
            if cur_node is not None:
                buf_sum -= cur_node

    # print('Answer:')
    # print(*res, sep='\n')
    # print(*res[::2], sep='\n')


tree = (1,
        (2,
         (3, None, None),
         (4, None, None)
         ),
        (5,
         (6, None, None),
         (7, None, None)
         )
        )

# tree = (1, (2, (3, None, None), None), None)
# find_path_sums(tree)
# print(res)

tree = (-938.51338, (1704.623214, (-651.093934, (-1158.202088, (243.108662, None, None), (-365.622307, None, None)),
                                   (-802.743718, (283.886211, None, None), (139.360217, None, None))), (
                         -2176.124231, (-1690.869603, (-766.025557, None, None), (731.075768, None, None)),
                         (-702.246092, (596.291331, None, None), (817.534604, None, None)))), (-1030.734792, (
    -417.402578, (2.637631, (1661.40228, None, None), (-350.320306, None, None)),
    (-603.017897, (745.223422, None, None), (-150.224439, None, None))), (-1313.814745,
                                                                          (1313.593324, (332.130276, None, None), None),
                                                                          (
                                                                              1036.39933, None,
                                                                              (508.181494, None, None)))))
find_path_sums(tree)