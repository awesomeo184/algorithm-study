from collections import defaultdict
from sys import stdin
from typing import Dict, List

numberOfVertexes, numberOfEdges = map(int, stdin.readline().split())

graph: Dict[int, List[int]] = defaultdict(list)

for i in range(numberOfEdges):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

numberOfGroups: int = 0
numberOfPeopleInGroup: List[int] = []
visited: List[bool] = [False] * numberOfVertexes

for vertex in range(numberOfVertexes):
    if visited[vertex]:
        continue
    else:
        stack: List[int] = [vertex]
        count: int = 0
        while stack:
            tmp: int = stack.pop()
            if not visited[tmp]:
                count += 1
                stack.extend(graph[tmp])
                visited[tmp] = True
        numberOfPeopleInGroup.append(count)
        numberOfGroups += 1

print(numberOfGroups)
print(max(numberOfPeopleInGroup), min(numberOfPeopleInGroup))