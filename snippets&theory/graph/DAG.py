

'''
8 11
5 1
1 2
1 4
4 6
6 2
6 7
2 7
4 0
0 6
3 0
5 3
'''
import sys


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.link = None


class Graph:
    def __init__(self, size):
        self.adjList = [None] * size
        self.visited = [False] * size
        self.n = size
        self.Long = [-sys.maxsize] * size  # 음의 무한대로 설정
        self.weight = {}  # 가중치 에지를 표현하기 위해 리스트가 아닌 딕셔너리 자료형 사용

    def add_edge(self, v1, v2, w):
        new_node = Node(v2)
        new_node.link = self.adjList[v1]
        self.adjList[v1] = new_node
        self.weight[str(v1) + str(v2)] = w

    def findLongestPath(self, v, t):  # v 시작점, t 목적지
        if v == t:
            self.Long[v] = 0
        node = self.adjList[v]
        while node is not None:
            w = node.vertex
            self.findLongestPath(w, t)
            self.Long[v] = max(self.Long[v], self.Long[w] + self.weight[str(v) + str(w)])
            node = node.link

    def printGraph(self):
        for v in range(self.n):
            print(v, end=": ")
            current = self.adjList[v]
            while current is not None:
                print(current.vertex, end=' ')
                current = current.link
            print()


n, m = [int(x) for x in input().split()]
g = Graph(n)
for i in range(m):
    v1, v2, w = [int(x) for x in input().split()]
    g.add_edge(v1, v2, w)
g.printGraph()
g.findLongestPath(5, 7)
print(g.Long)
# 8 11
# 5 1 2
# 5 3 7
# 1 4 7
# 1 2 9
# 3 0 8
# 4 0 7
# 4 6 9
# 0 6 3
# 6 2 4
# 6 7 6
# 2 7 3

# [10, 24, 3, 18, 17, 26, 7, 0]