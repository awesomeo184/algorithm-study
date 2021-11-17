# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        letter_logs.extend(digit_logs)

        return letter_logs

a = Solution()
print(a.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))