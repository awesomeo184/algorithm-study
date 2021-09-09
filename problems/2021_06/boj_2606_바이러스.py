from typing import Dict, List

# 백준 2606 - 바이러스
def solution(graph: Dict[int, List[int]], start: int):
    global count, visited
    visited[start]: int = 1
    for node in graph[start]:
        if visited[node] != 1:
            count += 1
            solution(graph, node)


visited: List[int]
count: int = 0

number_of_vertexes: int = int(input())
number_of_edges: int = int(input())

graph: Dict[int, List[int]] = {vertex: [] for vertex in range(1, number_of_vertexes+1)}
visited = [0 for _ in range(number_of_vertexes + 1)]

for _ in range(number_of_edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

solution(graph, 1)
print(count)