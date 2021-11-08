# https://programmers.co.kr/learn/courses/30/lessons/17687
# 진법 변환

def solution(n, t, m, p):
    answer = ''

    total = []

    for i in range(t*m):
        tmp = conversion(i, n)
        total.append(tmp)

    sequence = "".join(total)

    for i in range(t):
        tmp = sequence[:m]
        answer += tmp[p-1]
        sequence = sequence[m:]

    return answer


def conversion(number, n):
    result = []
    current = number

    if number == 0:
        result.append(0)

    while current > 0:

        if current % n < 10:
            result.append(current % n)
        else:
            result.append(chr(current % n - 10 + ord("A")))

        current //= n

    result = reversed(result)
    return "".join(map(str, result))
