"""
https://www.acmicpc.net/problem/2579


"""
from typing import List

N: int = int(input())
memo: List[int] = [0 for _ in range(N + 1)]
costs: List[int] = [0 for _ in range(N + 1)]
for i in range(N):
    costs[i + 1] = int(input())

if N == 1:
    memo[1] = costs[1]
elif N == 2:
    memo[2] = costs[1] + costs[2]
elif N == 3:
    memo[3] = max(costs[3] + costs[1], costs[3] + costs[2])
else:
    memo[1] = costs[1]
    memo[2] = costs[1] + costs[2]
    memo[3] = max(costs[3] + costs[1], costs[3] + costs[2])
    for step in range(4, N + 1):
        memo[step] = max(costs[step] + costs[step - 1] + memo[step - 3], costs[step] + memo[step - 2])
print(memo.pop())
