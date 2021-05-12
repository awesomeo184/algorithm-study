from typing import List


# * 주의사항: 시간 복잡도 O(n), 나누기 연산자 x
def solution(nums: List[int]) -> List[int]:
    p = 1
    out = []
    # 자신의 왼쪽 요소를 곱한 값
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    # 자신의 오른쪽 요소를 곱한 값
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out

'''
자신의 앞 인덱스의 요소에 대한 무언가가 필요할 때,
배열에 먼저 삽입하고 그 뒤에 연산.
즉 연산 후 바로 인덱스가 증가하도록 코드를 짜면됨
'''
