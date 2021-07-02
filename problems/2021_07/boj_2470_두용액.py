"""
생각의 과정

배열 내 두 값을 더했을 때 0에 가장 가까운 경우를 찾는 전형적인 투 포인터 문제이다.

배열을 오름차순으로 정렬한 후 양쪽 끝에 포인터를 두고 합을 구했을 때,
양수라면 값을 줄여야하니 오른쪽 포인터를, 음수라면 값을 늘려야하니 왼쪽 포인터를 옮겨준다.

그러면서 두 값의 합의 절대값의 최솟값을 저장한다. 이때 포인터가 가리키는 요소도 저장한다.

양 포인터가 엇갈리면 루프를 탈출한다.
"""
import sys
from typing import List, Tuple


def solution(liquid: List[int]) -> Tuple[int, int]:
    liquid.sort()

    left: int = 0
    right: int = len(liquid) - 1
    min_val: int = sys.maxsize
    answer_1: int = 0
    answer_2: int = 0

    while left < right:
        sum_val: int = liquid[left] + liquid[right]

        min_val = min(min_val, abs(sum_val))

        if abs(sum_val) == min_val:
            answer_1 = liquid[left]
            answer_2 = liquid[right]

        if sum_val == 0:
            answer_1 = liquid[left]
            answer_2 = liquid[right]
            break

        if sum_val > 0:
            right -= 1
        else:
            left += 1

    return (answer_1, answer_2) if answer_1 < answer_2 else (answer_2, answer_1)


N = int(input())

liquid = list(map(int, sys.stdin.readline().rstrip().split()))

a, b = solution(liquid)

print(a, b)
