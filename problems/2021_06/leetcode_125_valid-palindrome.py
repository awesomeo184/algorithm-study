"""
https://leetcode.com/problems/valid-palindrome/

가장 먼저 생각해볼 수 있는 방법은 문자열을 반대로 뒤집어서 같은지 확인하는 것이다.
문자열을 바로 뒤집는 법은 생각나지 않으므로 우선 문자열을 쪼개서 리스트로 만든다.

1. 리스트로 변환하기
    문자열을 순회하며 알파벳 혹은 숫자이면 lowercase로 바꿔서 빈 배열에 추가한다.
2. 해당 리스트를 뒤집은 리스트를 만든다
3. 두 리스트를 비교하며 요소와 순서가 같은지 확인한다.

Algorithm isValidPalindrome(targetString) -> boolean:
    arr = []

    for char in targetString:
        if char.isAlphaNumeric():
            arr.append(char.lowercase())

    reversedArr = arr.reverse()

    for i in range(len(arr)):
        if arr[i] != reversedArr[i]:
            return False
    return True
"""
import collections
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr: List = []

        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        reversedArr: List = list(reversed(arr))

        for i in range(len(arr)):
            if arr[i] != reversedArr[i]:
                return False

        return True
