"""
https://www.acmicpc.net/problem/11497

배열의 인접한 요소의 차의 최댓값이 최소가 되도록 했을 때 그 최댓값을 반환

생각의 과정

입력 배열의 최댓값을 계속 pop하면서 첫번째 pop한 값을 중앙, 이후로 왼쪽, 오른쪽 순으로 박음

1,2,3,4,5이면 2,4,5,3,1이 되도록 정렬

가장 차이가 적게 나도록 정렬되었기 때문에 차의 최댓값 구함

Algorithm solution(arr):
    arr = heapify(arr)

    i = 0
    left, center, right = [], [], []
    elem = arr.pop()
    center.append(elem)


    while len(arr) > 0:
        elem = arr.pop()

        if i is odd:
            left.append(elem)
        else:
            right.append(elem)

    left.reverse()

    result = left + center + right

    max_diff = 0
    for i in range(1, len(result)):
        diff = abs(arr[i-1] - arr[i])
        max(max_diff, diff)

    return max_diff

"""
import heapq
from typing import List


def solution(arr: List) -> int:
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, -num)

    i = 0
    left, center, right = [], [], []

    elem = heapq.heappop(max_heap) * -1
    center.append(elem)

    while len(max_heap) > 0:
        elem = heapq.heappop(max_heap) * -1

        if i % 2 == 0:
            left.append(elem)
        else:
            right.append(elem)

        i += 1

    left.reverse()
    result = left + center + right

    max_diff = 0
    for i in range(1, len(result)):
        diff = abs(result[i-1] - result[i])
        max_diff = max(max_diff, diff)

    return max_diff


T = int(input())

for _ in range(T):
    n = int(input())
    input_arr = list(map(int, input().split()))
    print(solution(input_arr))
