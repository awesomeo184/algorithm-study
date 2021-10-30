# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    tokens = [
        ["one", "1"],
        ["two", "2"],
        ["three", "3"],
        ["four", "4"],
        ["five", "5"],
        ["six", "6"],
        ["seven", "7"],
        ["eight", "8"],
        ["nine", "9"]
    ]

    for token in tokens:
        s = s.replace(token[0], token[1])

    return int(s)