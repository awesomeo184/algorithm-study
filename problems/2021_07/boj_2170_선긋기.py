"""
https://www.acmicpc.net/problem/2170


틀림:
    처음에는 도화지의 최종 상태를 구한 다음 최종적으로 정답을 계산하려고 했음.
    근데 start를 기준으로 정렬하고 선이 들어올 때마다 길이를 합친 후에 겹치면 겹친 구간만큼 빼주는 방식으로 하면 됨.

    start를 기준으로 정렬하면 순차적으로 해결할 수 있는 거를 생각못함

"""
import sys
from typing import List, Tuple


def solution(lines: List[Tuple[int, int]]) -> int:
    answer = 0

    lines.sort()

    prev_start = 0
    prev_end = 0

    for start, end in lines:
        if answer == 0:
            answer += (end - start)
            prev_start = start
            prev_end = end
            continue

        # 이전 구간에 완전히 포함되는 경우 더하지 않는다.
        if prev_start <= start and prev_end >= end:
            continue

        answer += (end - start)

        # 겹치는 구간이 있는 경우, 겹친만큼 다시 빼준다.
        if prev_end > start:
            answer -= (prev_end - start)

        prev_start = start
        prev_end = end
    return answer


lines: List[Tuple[int, int]] = []

n = int(input())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    lines.append((start, end))

print(solution(lines))
