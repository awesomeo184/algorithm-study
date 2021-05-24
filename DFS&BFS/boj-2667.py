from typing import List

# 백준 2667 단지 번호 붙이기
# 엣지 케이스를 항상 고려하자...
def DFS(graph: List[List[int]], x: int, y: int):
    global n, count, dx, dy
    for i in range(4):
        nx: int = x + dx[i]
        ny: int = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            count += 1
            DFS(graph, nx, ny)


def solution(graph: List[List[int]]):
    global n, count, answer
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # 방문처리 해줘야됨: 단지에 집이 하나인 경우
                count = 1
                graph[i][j] = 0
                DFS(graph, i, j)
                answer.append(count)


n: int = int(input())
count: int = 0
answer: List = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph: List[List[int]] = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

solution(graph)
answer.sort()

print(len(answer))
for i in answer:
    print(i)
