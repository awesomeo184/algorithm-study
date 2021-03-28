def solution1(string: str) -> bool:
    return string == string[::-1]


def solution2(string: str) -> bool:
    length: int = len(string) // 2

    for i in range(length):
        if not string[i] == string[len(string) - 1 - i]:
            return False

    return True
