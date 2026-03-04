visited = [[0]*5 for _ in range(5)]

def dfs(x, y, jug1, jug2, target):

    if visited[x][y]:
        return

    visited[x][y] = 1

    print("State:", (x, y))

    if x == target or y == target:
        print("Goal Reached")
        return

    dfs(jug1, y, jug1, jug2, target)
    dfs(x, jug2, jug1, jug2, target)
    dfs(0, y, jug1, jug2, target)
    dfs(x, 0, jug1, jug2, target)

    pour = x if x < jug2 - y else jug2 - y
    dfs(x - pour, y + pour, jug1, jug2, target)

    pour = y if y < jug1 - x else jug1 - x
    dfs(x + pour, y - pour, jug1, jug2, target)


dfs(0, 0, 4, 3, 2)