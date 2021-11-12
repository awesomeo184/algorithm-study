from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(progresses) > 0:
        count = 0
        while progresses[0] < 100:
            progresses = deque(map(sum, zip(progresses, speeds)))

        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        answer.append(count)

    return answer
