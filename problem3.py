n = int(input())
prices = list(map(int, input().split()))

max_count = 0
count = 0

for i in range(len(prices)-1):
    # 주식 가격이 다음날 올랐다면 count를 올린다.
    if prices[i] < prices[i+1]:
        count += 1
        # 카운트가 올라갈 때마다 최대값을 갱신한다.
        max_count = max(max_count, count)
    else:
        # 주식 가격이 다음 날 내려간다면, count를 초기화 한다.
        count = 0

print(max_count)