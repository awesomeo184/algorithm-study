from collections import defaultdict, deque
from sys import stdin
from typing import Dict, List, Deque

numberOfVertexes, numberOfEdges = map(int, stdin.readline().split())

graph: Dict[int, List[int]] = defaultdict(list)
visited: List[bool] = [False] * numberOfVertexes
distance: List[int] = [0] * numberOfVertexes
for i in range(numberOfEdges):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

stationA, stationB = map(int, stdin.readline().split())

def BFS(start: int, target: int) -> int:
    queue: Deque[int] = deque()
    queue.append(start)

    while queue:
        tmp: int = queue.popleft()
        if tmp == target:
            return distance[target]
        for vertex in graph[tmp]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                distance[vertex] = distance[tmp] + 1

    return -1

result: int = BFS(stationA, stationB)
print(result)