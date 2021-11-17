# https://leetcode.com/problems/most-common-word/
from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        tokens = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counter = Counter(tokens)
        return counter.most_common(1)[0][0]