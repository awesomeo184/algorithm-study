from typing import List


# https://leetcode.com/problems/trapping-rain-water/
def trap(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0

    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]

    while left < right:

        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
