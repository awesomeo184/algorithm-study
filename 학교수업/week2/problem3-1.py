n = int(input())

# 절대 시각(누적 시간)
absolute_time = []
time_stamp = 0
wait = 0

# 심사에 걸리는 시간
work_time = []

# 일이 끝난 실제 시간
work_end_time = []
for i in range(n):
    # 도착 상대 시간, 심사 시간
    arrived, work = map(int, input().split(" "))

    if i == 0:
        # 첫 번째 심사는 대기 시간이 없으므로
        work_end_time.append(work)

    time_stamp += arrived
    absolute_time.append(time_stamp)
    work_time.append(work)


for i in range(1, n):

    # 이전 작업이 현재 시간보다 늦게 끝나면
    if work_end_time[i-1] > absolute_time[i]:
        wait += (work_end_time[i-1] - absolute_time[i])

        work_end_time.append(work_end_time[i-1] + work_time[i])
    else:
        # 아니라면 기다린 시간 없이 작업 시간만 추가
        work_end_time.append(absolute_time[i] + work_time[i])

print(round(wait/n, 1))