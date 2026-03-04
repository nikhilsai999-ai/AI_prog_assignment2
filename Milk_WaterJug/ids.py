def DLS(node, depth, limit):

    if depth > limit:
        return

    print(node, end=" ")

    DLS(node*2, depth+1, limit)
    DLS(node*2+1, depth+1, limit)


def IDDFS(maxDepth):

    for i in range(maxDepth + 1):

        print("\nDepth", i, ":", end=" ")
        DLS(1, 0, i)


maxDepth = 3

IDDFS(maxDepth)