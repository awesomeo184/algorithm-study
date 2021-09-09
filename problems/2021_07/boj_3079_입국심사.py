"""

입국심사대를 최소 힙으로 관리
우선순위는 현재 심사 종료 시간 + 심사대의 심사 시간
"""

import sys
from collections import OrderedDict
from typing import List

N, people = map(int, input().split())
minEndTime: int = sys.maxsize
endTime: int = 0

cost2EndTimeMap = OrderedDict()

costs: List[int] = []
for _ in range(N):
    costs.append(int(sys.stdin.readline().rstrip()))

costs.sort()
for cost in costs:
    cost2EndTimeMap[cost] = 0


while people > 0:
    min_key = 0
    minEndTime = sys.maxsize
    for key, val in cost2EndTimeMap.items():
        minEndTime: int = min(minEndTime, val + key)
        if minEndTime == val+key:
            min_key = key
            endTime = val + key
    cost2EndTimeMap[min_key] = endTime
    people -= 1

print(endTime)