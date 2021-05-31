import sys
from collections import deque
from typing import Deque, List

# 숨바꼭질(https://www.acmicpc.net/problem/1697)
n, k = map(int, sys.stdin.readline().split())

distance: List[int] = [0 for _ in range(100_001)]


def BFS(start: int, target: int):
    queue: Deque[int] = deque()
    queue.append(start)
    while queue:
        tmp: int = queue.popleft()

        if tmp == target:
            print(distance[tmp])
            break

        offset: List[int] = [tmp - 1, tmp + 1, tmp * 2]

        for x in offset:
            if 0 <= x < 100_001 and not distance[x]:
                distance[x] = distance[tmp] + 1
                queue.append(x)


BFS(n, k)


# 이건 왜 안되는걸까...

# import sys
# from collections import deque
# from typing import Deque, List
#
# n, k = map(int, sys.stdin.readline().split())
#
# visited: List[int] = [0 for _ in range(100_000)]
#
# def BFS(start: int, target: int) -> int:
#     queue: Deque[int] = deque()
#     answer: int = 0
#     level: int = 0
#     queue.append(start)
#     while queue:
#         length: int = len(queue)
#         for i in range(length):
#             tmp: int = queue.popleft()
#
#             offset = [tmp-1, tmp+1, tmp*2]
#
#             for j in offset:
#                 if j == target:
#                     answer = level + 1
#                     return answer
#                 if 0 <= j < 100_001 and not visited[j]:
#                     queue.append(j)
#                     visited[j] = True
#         level += 1
#
# print(BFS(n, k))

