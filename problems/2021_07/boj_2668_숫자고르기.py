"""

생각의 과정

위의 집합과 아래 집합이 같으려면...

맵을 구성해서, K를 검색했을 때, T가 나왔다면 T를 검색했을 때 K가 나와야함.
혹은 K를 검색했을 때, K가 나와야한다.

Algorithm solution(map):
    input: 1부터 N까지가 key, 입력된 순서대로 값을 저장한 맵

    answer = []

    K = map[i]
    T = map[k]
    if T == i or K == i:
        answer.append(i)
"""
from typing import Dict, List


def solution(num_table: Dict[int, int]) -> List:
    answer: List[int] = []

    for i in range(1, len(num_table) + 1):
        K: int = num_table[i]
        T: int = num_table[K]

        if T == i or K == i:
            answer.append(i)

    answer.sort()
    return answer


N = int(input())

num_table = {}

for i in range(1, N + 1):
    num_table[i] = int(input())

answer = solution(num_table)

print(len(answer))
for i in answer:
    print(i)
