"""
https://www.acmicpc.net/problem/1946

생각의 과정.

다른 사람보다 서류 등수와 면접 등수가 모두 낮으면 탈락이다.
그럼 우선 서류 등수로 오름차순으로 정렬한 다음 앞에서 뒤로 순회하면서 앞보다
면접 등수가 낮다면, 서류 등수와 면접 등수 모두 낮다는 것이다.(이것이 타당한가?)

그 수를 세서 전체 인원에서 빼주면 합격 가능한 최대 인원이 도출된다.

정렬시간이 O(nlogn)이고 불합격자를 세는게 O(n)이므로 시간복잡도는 O(nlogn)


"""
import sys
from typing import List, Tuple


def solution(arr: List[Tuple]) -> int:
    # count_defeat: int =
    count = 1

    arr.sort()
    min = arr[0][1]

    for i in range(1, len(arr)):

        # interview_rank_of_current_elem: int = arr[i][1]
        # interview_rank_of_next_elem: int = arr[i + 1][1]
        # if interview_rank_of_next_elem > interview_rank_of_current_elem:
        #     count_defeat += 1
        if arr[i][1] < min:
            min = arr[i][1]
            count +=1
    # return len(arr) - count_defeat
    return count

number_of_test_case: int = int(input())
results: List[int] = []
for _ in range(number_of_test_case):
    n: int = int(input())
    info_list: List[Tuple] = []
    for _ in range(n):
        info_list.append(tuple(map(int, sys.stdin.readline().split())))
    results.append(solution(info_list))

for i in results:
    print(i)