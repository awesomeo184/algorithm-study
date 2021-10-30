# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
# 윈도우, 시간문자열


def solution(lines):
    answer = 1
    logs = []

    for line in lines:
        date, response_time, duration = line.split(" ")
        logs.append(transform_to_log_format(response_time, duration))

    for log in logs:
        base_start = log[0]
        base_end = log[1]
        answer = max(answer, throughput(base_start, base_start + 1, logs), throughput(base_end, base_end + 1, logs))

    return answer


def transform_to_log_format(response_time, duration):
    end_time = hhmmss_to_double(response_time)
    duration = second_to_double(duration)
    start_time = end_time - duration + 0.001
    return [start_time, end_time]


def hhmmss_to_double(time):
    hour, minute, second = time.split(":")

    hour = float(hour) * 3600
    minute = float(minute) * 60
    second = float(second)

    return hour + minute + second


def second_to_double(time):
    return float(time[:-1])


def throughput(start, end, logs):
    count = 0

    for log in logs:
        start_compare = log[0]
        end_compare = log[1]

        if start_compare < end and end_compare >= start:
            count += 1
    return count