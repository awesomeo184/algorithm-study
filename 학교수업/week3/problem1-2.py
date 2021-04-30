n = int(input())
cost = list(map(int, input().rstrip(" ").split(" ")))

# dp[k] = k 번째 계단까지 오르는데 드는 최소 비용
# dp[0]은 빈칸
dp = [0 for _ in range(n + 1)]

# n이 5 이하인 경우는 직접 구한 뒤 저장한다.
dp[1] = cost[0]
if n > 1:
    dp[2] = cost[0] + cost[1]
if n > 2:
    dp[3] = cost[2]
if n > 3:
    dp[4] = cost[3]

# 계단을 오르는 비용은 계속 누적되므로 아래부터 계속 최소비용을 누적하면서 n까지 올라간다.
for i in range(5, n + 1):
    dp[i] += min(dp[i - 1], dp[i - 3], dp[i - 4]) + cost[i - 1]


print(dp[-1])