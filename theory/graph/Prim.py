from queue import PriorityQueue


def prim(adj, start):
    # T에 포함된 정점을 표시하기 위한 변수
    covered = set()

    # prim 알고리즘의 결과 그래프를 리턴하기 위한 변수
    res_edges = []

    # 후보 간선을 관리하기 위한 우선 순위 큐, 후보간선(가중치, 목적 정점, 시작 정점)
    queue = PriorityQueue()
    queue.put((0, start, None))

    while not queue.empty():
        # 최소 가중치를 가지는 간선 정보
        u_cost, u, u_src = queue.get()

        # 이미 T에 포함되어 있다면 넘어간다
        if u in covered:
            continue

        covered.add(u)

        # u_src가 None인 경우는 간선이 아닌 첫번째 큐에 넣은 특별한 값이므로 무시
        if u_src is not None:
            res_edges.append((u_cost, u, u_src))

        # 정점 u와 연결된 모든 간선 (u,v) 중 v가 T에 포함되지 않은 경우에만 후보 간선에 넣어준다.
        for v_cost, v in adj[u]:
            if v not in covered:
                queue.put((v_cost, v, u))

    return res_edges


graph = {
    "a": [(4, "b"), (3, "c")],
    "b": [(4, "a"), (2, "c"), (7, "d")],
    "c": [(3, "a"), (2, "b"), (5, "d"), (11, "e")],
    "d": [(7, "b"), (5, "c"), (2, "e"), (8, "f")],
    "e": [(11, "c"), (2, "d"), (9, "f")],
    "f": [(8, "d"), (9, "e")]
}

res_edges = prim(graph, "a")

for u_cost, u, v in res_edges:
    print(u, " - ", v, " : ", u_cost)