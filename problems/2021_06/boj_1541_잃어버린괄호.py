"""
https://www.acmicpc.net/problem/1541

생각의 과정

연산의 결과가 최소값이 되려면 빼주는 값을 최대한 크게 만들면 된다.

"-" 가 제일 처음 등장하면 그 뒤에 등장하는 연산이 무엇이든 간에 뺄셈으로 만들 수 있다.

덧셈은 결합 법칙이 성립하므로 덧셈 기호가 나타나면 제일 처음 나타난 "-" 기호 뒤의 수와 더해준다.
뺄셈 기호가 나타나면 어차피 그냥 빼주면 되기 때문에 제일 처음 나타난 "-" 기호 뒤의 수와 더해준다.

즉 입력값을 리스트에 담아서 첫 번째 "-"가 나타날 때까지 등장하는 숫자들은 모두 plusStack에 담아준다.
"-"가 등장했다면 그 이후에 등장하는 숫자들은 모두 minusStack에 넣어준다.

리스트를 모두 순회하면 sum(plusStack) - sum(minusStack)을 반환한다.
"""


import collections
from typing import Deque, List


def split_expr(expr: str) -> Deque:
    result = collections.deque()
    tmp = ""
    i = 0
    while i < len(expr):
        if expr[i] == "+" or expr[i] == "-":
            result.append(tmp)
            result.append(expr[i])
            tmp = ""
        else:
            tmp += expr[i]
        i += 1
    result.append(tmp)
    return result


def solution(expr: str) -> int:
    plusStack: List[int] = []
    minusStack: List[int] = []
    inputMinusStack = False

    symbols = split_expr(expr)

    while len(symbols) != 0:
        symbol: str = symbols.popleft()

        if symbol == "-":
            inputMinusStack = True
            continue

        if inputMinusStack and symbol.isdigit():
            minusStack.append(int(symbol))
            continue

        if not inputMinusStack and symbol.isdigit():
            plusStack.append(int(symbol))

    return sum(plusStack) - sum(minusStack)


print(solution(input()))
