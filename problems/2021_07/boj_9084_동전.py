"""
https://www.acmicpc.net/problem/9084

"""

T = int(input())


def solution(N, coins, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    for coin in coins:
        for step in range(target+1):
            if step - coin >= 0:
                dp[step] += dp[step-coin]
    return dp[-1]


for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    print(solution(N, coins, target))