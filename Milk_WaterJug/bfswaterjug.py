visited = [[0]*5 for _ in range(5)]

class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


queue = [Node() for _ in range(100)]
front = 0
rear = 0


def enqueue(x, y):
    global rear
    queue[rear].x = x
    queue[rear].y = y
    rear += 1


def dequeue():
    global front
    node = queue[front]
    front += 1
    return node


def isEmpty():
    return front == rear


def bfs(jug1, jug2, target):

    enqueue(0, 0)
    visited[0][0] = 1

    while not isEmpty():

        temp = dequeue()
        x = temp.x
        y = temp.y

        print("State:", (x, y))

        if x == target or y == target:
            print("Goal Reached")
            return

        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - (jug2 - y if jug2 - y < x else x),
             y + (jug2 - y if jug2 - y < x else x)),
            (x + (jug1 - x if jug1 - x < y else y),
             y - (jug1 - x if jug1 - x < y else y))
        ]

        for i in range(6):

            a = states[i][0]
            b = states[i][1]

            if a >= 0 and b >= 0 and a <= jug1 and b <= jug2 and not visited[a][b]:
                visited[a][b] = 1
                enqueue(a, b)


bfs(4, 3, 2)