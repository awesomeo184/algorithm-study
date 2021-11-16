# 파일명 정렬 https://programmers.co.kr/learn/courses/30/lessons/17686
# 문자열 처리, 정규식 고려

from typing import List


def solution(files: List[str]):

    preprocessed = []

    for file in files:

        # ["foo99999sdfef", "txt"] or ["F-15"]
        tokens = file.split(".")

        former = ""
        extension = ""

        head = ""
        number = ""
        tail = ""

        if len(tokens) > 1:
            former = tokens[0]
            extension = tokens[1]
        else:
            former = tokens[0]

        # former에서 HEAD와 NUMBER를 분리. 나머지는 extension과 합쳐 TAIL로 만든다.
        i = 0
        while not former[i].isdigit():
            head += former[i]
            i += 1

        count = 0
        while i < len(former) and count < 5 and former[i].isdigit():
            number += former[i]
            count += 1
            i += 1

        if len(former) > i + 1:
            if extension:
                tail = former[i:] + "." + extension
            else:
                tail = former[i:]
        else:
            if extension:
                tail = "." + extension


        preprocessed.append([head, number, tail])

    preprocessed.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return list(map(lambda x: x[0]+x[1]+x[2], preprocessed))
