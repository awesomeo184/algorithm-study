from typing import List


# https://leetcode.com/problems/two-sum/
def twoSum(nums: List[int], target: int) -> List[int]:
    table = {}
    # * 엣지케이스: [3, 3], 6
    for index, n in enumerate(nums):
        table[n] = index

    for index, n in enumerate(nums):
        # * 같은 key가 value인 index를 덮어쓰면 현재 인덱스와 달라지므로 처리 가능
        if target - n in table and index != table[target - n]:
            return [nums.index(n), table[target - n]]

