import heapq


def get_waiting_line(n):
    waiting_line = []
    count = 0
    for i in range(n):
        arrived, exam = map(int, input().rstrip(" ").split(" "))
        # 누적 시간 계산 (도착한 절대 시각)
        count += arrived
        waiting_line.append([count, exam])
    return waiting_line


def get_and_count_waiting_time(min_node, person):
    global total_waiting_time

    exit_time_of_prev = min_node[0]
    arrived_time = person[0]

    waiting_time = exit_time_of_prev - arrived_time
    if waiting_time < 0:
        waiting_time = 0

    total_waiting_time += waiting_time

    return waiting_time


def is_exam_table_full(exam_line):
    return len(exam_line) >= k


def push_in_heap(exam_line, person):
    waiting_time = 0
    if is_exam_table_full(exam_line):
        min_node = heapq.heappop(exam_line)
        # 대기 시간 = 앞사람 종료 시간 - 내 도착시간 (0보다 작으면 0)
        waiting_time = get_and_count_waiting_time(min_node, person)

    # 종료 시간 = 대기시간 + 내 도착시간 + 내 작업시간
    exit_time = waiting_time + person[0] + person[1]

    heapq.heappush(exam_line, (exit_time, person[0], person[1]))


total_waiting_time = 0
exam_line = []

k = int(input())
n = int(input())

waiting_line = get_waiting_line(n)
for person in waiting_line:
    push_in_heap(exam_line, person)

print(round(total_waiting_time / n, 1))
