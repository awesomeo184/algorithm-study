import sys

n = int(input())
prices = list(map(int, input().split()))

profit = 0
min_price = sys.maxsize

sell_price = 0
buy_price = 0

for price in prices:
    # 루프를 순회하면서 최소값을 갱신한다.
    min_price = min(min_price, price)

    # price - min_price = 현재 가리키고 있는 요소(오늘 주식 가격) - 최소값 = 수익금
    # 수익금을 최대값으로 갱신한다.
    profit = max(profit, price - min_price)

    # 만약 현재 수익금이 최대 수익금이라면, 사는 금액과 파는 금액을 저장한다.
    if profit == price - min_price:
        sell_price = price
        buy_price = min_price

# 수익이 없다면 -1을 출력한다.
if profit == 0:
    print(-1)
else:
    print(profit)
    print(buy_price, sell_price)

