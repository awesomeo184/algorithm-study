import copy
from sys import stdin
from typing import List

n, m = map(int, stdin.readline().split())
graph: List[List[int]] = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(n)]

# 상하좌우의 셀을 확인하기 위한 변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# -1로 초기화 한 후, 경로가 존재하면 1 할당
answer = -1

# 셀 하나를 의미하는 Point 자료형 선언
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def DFS(x: int, y: int):
    global n, m, dx, dy, answer, graph
    stack = []

    # 방문 처리를 위해 해당 요소를 이동 불가능한 상태(0)로 만든다.
    # 이때 그래프를 직접 바꾸면 다음 for-loop에서 제대로 탐색할 수 없으므로
    # 매 반복마다 graph를 deep copy한 배열을 이용한다.
    copy_graph = copy.copy(graph)

    # 이동이 불가능한 경우(해당 요소가 0) 바로 리턴해 탐색하지 않는다.
    if x == 0 and graph[x][y] == 0:
        return
    else:
        stack.append(Point(x, y))
        # 첫 요소 graph[0][i]에 대해 방문처리한다.
        copy_graph[x][y] = 0
        while stack:
            node: Point = stack.pop()

            # 선택된 요소의 상하좌우 셀을 살핀다.
            for i in range(4):
                nx: int = node.x + dx[i]
                ny: int = node.y + dy[i]

                # 상하좌우 셀이 배열의 범위를 벗어나지 않고 이동 가능하다면 탐색한다.
                if 0 <= nx < n and 0 <= ny < m and copy_graph[nx][ny] == 1:
                    # 만약 마지막 행이라면 마지막 행까지 이동가능한 경로가 존재한다는 뜻이므로 답을 반환한다.
                    if nx == n - 1:
                        answer = 1
                        return
                    # 해당 셀을 방문처리 후 스택에 담아 다음 반복에서 다시 탐색한다.
                    copy_graph[nx][ny] = 0
                    stack.append(Point(nx, ny))


for i in range(m):
    DFS(0, i)
    # 이전 탐색에서 답을 발견했다면 더이상 탐색하지 않고 리턴한다.
    if answer == 1:
        break

print(answer)
