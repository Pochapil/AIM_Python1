def find_path_sums(tree):
    stack = [tree]
    val_stack = []
    flag = True
    while stack:
        # print(stack)
        #print('stack:', end=' ')
        #print(stack)
        cur_node = stack.pop()
        # print(cur_node)
        if isinstance(cur_node, tuple):
            if not flag:
                flag = True
                # val_stack.pop()
            val = cur_node[0]
            #print(val)
            # res.append(val)
            left = cur_node[1]
            right = cur_node[2]
            val_stack.append(val)

            stack.append(right)
            stack.append(val)
            stack.append(left)

            print(val_stack)
        else:
            if flag:
                flag = False
                val_stack.pop()
            # print(cur_node)
            # if cur_node is not None:
                # val_stack.pop()
            #print(val_stack)
            # val_stack.append(cur_node)

            # print('pop?')
            # val = cur_node
            # print(val)
    # print(res)


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
