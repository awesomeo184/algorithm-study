from typing import List


def array_partition(nums: List[int]) -> int:
    nums.sort()
    answer: int = 0
    for i in range(0, len(nums), 2):
        answer += nums[i]
    return answer
