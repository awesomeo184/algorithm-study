# https://programmers.co.kr/learn/courses/30/lessons/12977

from math import sqrt
from itertools import combinations


def solution1(nums):
    answer = 0

    n = len(nums)

    for i in range(n):
        a = nums[i]
        for j in range(i + 1, n):
            b = nums[j]
            for k in range(j + 1, n):
                c = nums[k]
                target = a + b + c
                if is_prime(target):
                    answer += 1

    return answer


def solution2(nums):
    answer = 0
    nums = [sum(x) for x in combinations(nums, 3)]
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(list(combinations([1, 2, 3, 4, 5], 2)))
