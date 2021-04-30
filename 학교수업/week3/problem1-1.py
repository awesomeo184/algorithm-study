n = int(input())

# k번째 계단을 올라가는 방법의 수 = dp[k]
# dp[0] 빈칸
dp = [0 for _ in range(n + 1)]

# n이 4이하인 경우는 직접 초기화해준다.
dp[1] = 1
if n > 1:
    dp[2] = 1
if n > 2:
    dp[3] = 2
if n > 3:
    dp[4] = 4

if n > 4:
    for i in range(5, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

print(dp[-1])
