import sys
from collections import deque
from typing import List, Deque, Tuple

# 토마토 (https://www.acmicpc.net/problem/7576)
m, n = map(int, sys.stdin.readline().split())

tomatoBox: List[List[int]] = []
for _ in range(n):
    tomatoBox.append(list(map(int, sys.stdin.readline().split())))

calendar = [[0 for _ in range(m)] for _ in range(n)]

dx: List[int] = [-1, 1, 0, 0]
dy: List[int] = [0, 0, 1, -1]


def BFS() -> int:
    global m, n, tomatoBox, dx, dy, calendar
    queue: Deque[Tuple] = deque()
    flag: bool = True
    answer: int = -1

    for x in range(n):
        for y in range(m):
            if tomatoBox[x][y] == 1:
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tomatoBox[nx][ny] == 0:
                tomatoBox[nx][ny] = 1
                calendar[nx][ny] = calendar[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if tomatoBox[i][j] == 0:
                flag = False
    if flag:
        for i in range(n):
            for j in range(m):
                answer = max(answer, calendar[i][j])
    return answer

print(BFS())
