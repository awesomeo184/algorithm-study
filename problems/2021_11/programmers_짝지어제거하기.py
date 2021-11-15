# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return 0 if len(stack) > 0 else 1