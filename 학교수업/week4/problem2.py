import sys
import copy

m, n = map(int, input().split())

cost = []

for i in range(m):
    cost.append(list(map(int, input().split())))


def solution(m, n, cost):
    if m < 2:
        return min(cost[-1])

    answer = copy.copy(cost[-1])

    dx = [-1, 0, 1]

    for i in range(m - 2, -1, -1):
        tmp = copy.copy(answer)
        for j in range(n):
            min_val = sys.maxsize
            for x in dx:
                #양 끝에 있는 셀의 경우 배열의 범위를 벗어나면 연산하지 않는다.
                if (j == 0 and x == -1) or (j == n - 1 and x == 1):
                    continue
                min_val = min(min_val, tmp[j+x])
            answer[j] = cost[i][j] + min_val
    return min(answer)


print(solution(m, n, cost))




# bottom-up 방식

def grid(i, m, n, C, A):   # 0, m, n, C, A
    if (i == 0):
        for j in range(n):  # 0, 1, 2, 3, 4
            A[j] = C[m-1-i][j] # base case
        return grid(i + 1, m, n, C, A)

    elif(i <= m-1): # (i <= m-1) && (i != 0)
        temp = []
        for j in range(n):  # i = 1, 2, 3
            if (j == 0 and j < n-1):
                temp.append(min(A[j], A[j+1]) + C[m-1-i][j]) # 맨 왼쪽에 셀이 위치하는 경우
            elif (j == n-1):
                temp.append(min(A[j-1], A[j]) + C[m-1-i][j]) # 맨 오른쪽에 셀이 위치하는 경우
            else: # (0 < j < n-1)
                temp.append(min(A[j-1], A[j], A[j+1]) + C[m-1-i][j]) # 그 외에 셀이 위치하는 경우
        A = temp
        if (i == m-1):
            print(min(A))
        else:
            return grid(i + 1, m, n, C, A)
    else:  #(i > m-1)
        print(min(A))


# m : 행, n : 열
m, n = map(int, input().split())

C = []
for i in range(m):
    C.append(list(map(int, input().split())))

A = []
for k in range(n):
    A.append(0)


grid(0, m, n, C, A)

