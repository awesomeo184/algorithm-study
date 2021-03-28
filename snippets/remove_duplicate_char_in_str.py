from typing import List


def solution(string: str) -> str:
    chars: List = [char for char in string]
    return "".join(list(dict.fromkeys(chars)))