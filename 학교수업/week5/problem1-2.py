from collections import deque
from sys import stdin, maxsize
from typing import Deque, List

n, m = map(int, stdin.readline().split())
graph: List[List[int]] = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(n)]
answer: List[int] = [maxsize] * m
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Point:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


def BFS(x: int, y: int, visited: List[List[bool]]):
    global n, m, graph, dx, dy, answer
    queue: Deque[Point] = deque()

    if graph[x][y] == 0:
        return
    else:
        queue.append(Point(x, y, 1))
    visited[x][y] = True
    while queue:
        tmp: Point = queue.popleft()

        for i in range(4):
            nx: int = tmp.x + dx[i]
            ny: int = tmp.y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                if visited[nx][ny]:
                    continue
                if nx == n - 1:
                    answer[y] = tmp.distance + 1
                    return
                visited[nx][ny] = True
                queue.append(Point(nx, ny, tmp.distance + 1))


for i in range(m):
    visited: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
    BFS(0, i, visited)

print(min(answer) if min(answer) < maxsize else -1)
print(answer)
