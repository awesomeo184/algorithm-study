# https://programmers.co.kr/learn/courses/30/lessons/72410
# 문자열 조작 메서드

from typing import List


def solution(new_id):
    return process(new_id)


def process(new_id):
    return first_step(new_id)


def first_step(new_id: str) -> str:
    return second_step(new_id.lower())


def second_step(new_id: str) -> str:
    result: str = ''
    allowed_char: List[str] = ['-', '_', '.']
    for s in new_id:
        if s.isalnum():
            result += s
        elif s in allowed_char:
            result += s
    return third_step(result)


def third_step(new_id: str) -> str:
    while new_id.find("..") != -1:
        new_id = new_id.replace("..", ".")

    return forth_step(new_id)


def forth_step(new_id: str) -> str:
    return fifth_step(new_id.strip("."))


def fifth_step(new_id: str) -> str:
    if new_id == '':
        new_id = 'a'

    return sixth_step(new_id)


def sixth_step(new_id: str) -> str:
    if len(new_id) >= 16:
        new_id = new_id[:15]

    return seventh_step(new_id.strip('.'))


def seventh_step(new_id: str) -> str:
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
