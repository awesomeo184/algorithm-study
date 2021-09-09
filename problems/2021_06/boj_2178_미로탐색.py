from collections import deque
from sys import stdin
from typing import Deque, List

# 백준-2178 미로탐색
# 인풋은 stdin.readline() 사용하자.
n, m = map(int, stdin.readline().split())
graph: List[List[int]] = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(n)]
distance: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def BFS(x, y):
    global n, m, graph, distance, dx, dy
    queue: Deque[Point] = deque()
    queue.append(Point(x, y))
    graph[x][y] = 0
    while queue:
        tmp: Point = queue.popleft()

        for i in range(4):
            nx: int = tmp.x + dx[i]
            ny: int = tmp.y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append(Point(nx, ny))
                distance[nx][ny] = distance[tmp.x][tmp.y] + 1


distance[0][0] = 1
BFS(0, 0)
print(distance[n - 1][m - 1])
