"""

생각의 과정

처음에 양 끝에 공유기를 하나씩 박고 중간에 박으면서 양 끝과의 거리를 계산하면서 카운트를 세는 방법을 생각했는데,
일단 구현이 너무 복잡하고 확인해야될 예외도 많았다. 접근을 잘못했음.

가능한 공유기의 거리를 이분탐색으로 늘렸다 줄였다 해보면서 가능한 최대값을 찾는 방식으로 탐색해야됨.

이분탐색의 대상 -> 공유기 거리
앞집에서부터 거리만큼 늘려가면서 카운트를 세고 목표한 공유기 개수만큼 설치했는지 확인

이 두 가지 접근을 떠올리는게 쉽지 않았다. 구현은 비교적 쉬운편.
"""


from typing import List


def solution(houses: List[int], target: int) -> int:
    houses.sort()
    start: int = 1
    end: int = houses[-1] - houses[0]
    answer = 0


    if target == 2:
        return end

    while start <= end:
        mid: int = (start + end) // 2
        count: int = 1
        house_pointer: int = houses[0]

        for i in range(len(houses)):
            if house_pointer + mid <= houses[i]:
                count += 1
                house_pointer = houses[i]

        if count >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))

print(solution(houses, C))