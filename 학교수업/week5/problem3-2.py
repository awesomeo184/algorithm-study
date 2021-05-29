from collections import defaultdict, deque
from sys import stdin
from typing import Dict, List, Deque


class Line:
    def __init__(self, lineNumber):
        self.lineNumber: str = lineNumber
        self.stations: Dict[str, List[str]] = defaultdict(list)

    def addStation(self, stationA: str, stationB: str):
        self.stations[stationA].append(stationB)
        self.stations[stationB].append(stationA)

    def searchPath(self, start: str, end: str) -> List[str]:
        queue: Deque = deque()
        path: List[str] = []
        visited: List[str] = []
        prev: Dict[str, str] = defaultdict(str)

        queue.append(start)
        while queue:
            tmp = queue.popleft()

            if tmp == end:
                path.append(tmp)
                return path
            else:
                if not tmp in visited:
                    visited.append(tmp)
                    queue.extend(self.stations[tmp])
                    for station in self.stations[tmp]:
                        prev[station] = tmp
        return []

    def __str__(self):
        return self.lineNumber


numberOfEdges = int(input())
lines: List[Line] = []

for _ in range(numberOfEdges):
    lineNumber, stationA, stationB = stdin.readline().split()

    flag: bool = True
    for line in lines:
        if str(line) == lineNumber:
            line.addStation(stationA, stationB)
            flag = False
    if flag:
        line: Line = Line(lineNumber)
        line.addStation(stationA, stationB)
        lines.append(line)

start, end = stdin.readline().split()

path = lines[0].searchPath(start, end)
print(path)
