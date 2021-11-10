# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail_rates = []
    total = len(stages)

    for i in range(1, N + 1):

        if total == 0:
            fail_rates.append((i, 0))
            continue

        count = stages.count(i)
        fail_rate = count / total
        fail_rates.append((i, fail_rate))
        total -= count

    fail_rates.sort(key=lambda x: (-x[1], x[0]))

    return list(map(lambda x: x[0], fail_rates))