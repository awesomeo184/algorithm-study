m, n = map(int, input().split(" "))

cost = []

for i in range(m):
    cost.append(list(map(int, input().split())))

answer=[]
if m < n:
    # answer 초기화
    answer = [cost[m - 1][0]] + [0 for _ in range(m-1)]

    # 첫 출 누적값 계산
    for i in range(1, m):
        answer[i] = answer[i - 1] + cost[m - i - 1][0]

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                answer[j] += cost[m-1][i]
            else:
                answer[j] = min(answer[j-1], answer[j]) + cost[m-j-1][i]

else:
    answer = [cost[m - 1][0]] + [0 for _ in range(n-1)]
    for i in range(1,n):
        answer[i] = answer[i-1] + cost[m-1][i]
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                answer[j] += cost[m-i-1][0]
            else:
                answer[j] = min(answer[j-1], answer[j]) + cost[m-i-1][j]

print(answer[-1])