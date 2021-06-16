import sys
import heapq

from collections import defaultdict
from typing import Dict, List, Tuple


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int):
    global distance

    # 최단거리가 확정된 노드를 꺼내기 위한 최소힙. 경로가 가장 작은 노드의 연결정보를 꺼내온다.
    # 튜플 내 순서가 (비용, 노드번호)인 이유는 나중에 heapq 에서 연산을 할때 튜플의 가장 첫번째 요소를 비교요소로 잡기 때문
    min_heap: List[Tuple[int, int]] = []

    # 시작노드에서 시작노드로 가는 비용은 0
    heapq.heappush(min_heap, (0, start))
    distance[start] = 0

    while len(min_heap) != 0:
        current_cost, current_node = heapq.heappop(min_heap)

        # 만약 현재 거리값이 기록된 거리값보다 크면 최단 거리일 여지가 없으므로 그냥 넘어간다.
        if distance[current_node] < current_cost:
            continue

        for adjacent_info in graph[current_node]:
            cost_to_adjacent_node: int = adjacent_info[0]
            adjacent_node: int = adjacent_info[1]

            # 현재 노드에서 인접한 노드로 이동할 때의 비용이 해당 노드의 현재 기록된 거리 값보다 작으면 값을 갱신한다.
            if distance[adjacent_node] > current_cost + cost_to_adjacent_node:
                distance[adjacent_node] = current_cost + cost_to_adjacent_node
                heapq.heappush(min_heap, (distance[adjacent_node], adjacent_node))


# input
# 첫 줄에 노드 수, 에지 수
# 둘째 줄부터 출발노드, 도착노드, 비용. 예를 들어 0, 1, 5가 주어지면 0번 노드에서 1번 노드로 이동할 수 있고 비용은 5이다.
'''
5 7
0 1 8
0 2 3
0 3 10
1 2 2
1 4 7
2 3 6
2 4 3
'''

num_of_node, num_of_edge = map(int, input().split())

# distance 배열의 모든 요소를 최댓값으로 초기화
distance: List[int] = [sys.maxsize for _ in range(num_of_node)]

# { 노드: 연결정보(비용, 노드번호)의 리스트 }
graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

# 그래프 정보 입력
for _ in range(num_of_edge):
    from_, to_, cost = map(int, input().split())
    graph[from_].append((cost, to_))

dijkstra(graph, 0)

# 출력
for i in range(num_of_node):
    print(i, ":", distance[i])