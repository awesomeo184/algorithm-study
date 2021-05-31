from typing import List

graph = {
    1: [2, 3, ],
    2: [4, 5, ],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: [],
}


def dfs(graph: dict, vertex: int, visited: List):
    visited[vertex] = True
    print(vertex, end=" ")

    for w in graph[vertex]:
        if not visited[w]:
            dfs(graph, w, visited)


visited = [False] * (len(graph.keys()) + 1)

dfs(graph, 1, visited)
