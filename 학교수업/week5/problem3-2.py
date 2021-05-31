from collections import defaultdict, deque
from sys import stdin
from typing import Dict, List, Deque, Set, Tuple

numberOfEdges = int(input())

graph: Dict[str, List[str]] = defaultdict(list)

# 지하철역: (속한 호선,)
stationToLineMap: Dict[str, Set[str]] = defaultdict(set)

# 지하철역: [이전 역, (현재 이동 중인 호선,)]
parent: Dict[str, List] = defaultdict(list)
stationToTransferCount: Dict[str, int] = defaultdict(int)
visited: Dict[str, bool] = defaultdict(bool)

for i in range(numberOfEdges):
    line, a, b = stdin.readline().split()
    graph[a].append(b)
    graph[b].append(a)
    stationToLineMap[a].add(line)
    stationToLineMap[b].add(line)
    visited[a] = False
    visited[b] = False

start, end = stdin.readline().split()


def traceback(station: str):
    result = []
    result.append(station)
    parentStation, line = parent[station]
    while parentStation:
        result.append(parentStation)
        parentStation, transfer = parent[parentStation]
    result.reverse()
    return result


def BFS(start: str, end: str):
    queue: Deque[str] = deque()
    queue.append(start)

    possibleAnswerSet: List = []

    parent[start] = ["", stationToLineMap[start]]
    visited[start] = True
    stationToTransferCount[start] = 0

    while queue:
        tmp: str = queue.popleft()

        for vertex in graph[tmp]:
            if vertex == end:
                parent[vertex] = [tmp, stationToLineMap[tmp] & stationToLineMap[vertex]]

                if len(stationToLineMap[vertex] & parent[tmp][1]) == 0:
                    stationToTransferCount[vertex] = stationToTransferCount[tmp] + 1
                else:
                    stationToTransferCount[vertex] = stationToTransferCount[tmp]

                possibleAnswer: Tuple[List[str], int] = (traceback(vertex), stationToTransferCount[vertex])
                possibleAnswerSet.append(possibleAnswer)
                continue

            if not visited[vertex]:

                parent[vertex] = [tmp, stationToLineMap[tmp] & stationToLineMap[vertex]]
                visited[vertex] = True
                queue.append(vertex)

                if len(stationToLineMap[vertex] & parent[tmp][1]) == 0:
                    stationToTransferCount[vertex] = stationToTransferCount[tmp] + 1
                else:
                    stationToTransferCount[vertex] = stationToTransferCount[tmp]



    return possibleAnswerSet


result: List[Tuple[List[str], int]] = BFS(start, end)

result = sorted(result, key=lambda x: (len(x[0]), x[1]))
if len(result) == 0:
    print(-1)
else:
    answer = result[0][0]
    print(len(answer))
    for station in answer:
        print(station, end=" ")
