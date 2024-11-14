def find_path_sums(tree):
    stack = []
    cur_node = tree
    left_idx = 1
    right_idx = 2
    i = 1
    # while cur_node is not None:
    #
    #     cur_node = tree[i]
    #     i += 1
    for cur_node in tree:
        left = cur_node[left_idx]
        right = cur_node[right_idx]
        print(cur_node, left, right)
        # stack.append(node)
    print(len(stack))


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
find_path_sums(tree)
