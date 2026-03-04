def DLS(node, depth, limit):

    if depth > limit:
        return

    print(node, end=" ")

    DLS(node*2, depth+1, limit)
    DLS(node*2+1, depth+1, limit)


limit = 3

print("Depth Limited Search Traversal:")

DLS(1, 0, limit)