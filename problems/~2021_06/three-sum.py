from typing import List


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]

                if summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1
                else:
                    # 정답 처리
                    answer.append([nums[i], nums[left], nums[right]])

                    # 같은거 스킵하고 계속 진행
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer

solution = Solution()

print(solution.threeSum([-1, 0, 1, 2, -1, -4]))