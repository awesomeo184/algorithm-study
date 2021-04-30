import sys

n, k = map(int, input().split(" "))
steps = list(map(int, input().rstrip(" ").split(" ")))
cost = list(map(int, input().rstrip(" ").split(" ")))

# 밟는 계단을 최소 비용으로 갱신하므로, 최대값으로 초기화한다.
dp = [sys.maxsize for _ in range(n + 1)]

# 시작 부분을 초기화한다.
# ex) 한 번에 올라갈 수 있는 계단의 수가 1, 3, 5로 주어지는 경우 dp[1], dp[3], dp[5]에 비용을 추가
for step in steps:
    dp[step] = cost[step-1]

for i in range(n):
    # 올라갈 수 있는 계단의 모든 경우의 수를 탐색하며 이때의 최소 비용을 구한다.
    for step in steps:
        if i + step < n + 1:
            dp[i+step] = min(dp[i+step], dp[i] + cost[i+step-1])

# 값이 갱신된 경우가 아니라면 -1을 출력한다.
print(dp[-1] if dp[-1] < sys.maxsize else -1)