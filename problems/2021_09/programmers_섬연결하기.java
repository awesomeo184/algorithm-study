package programmers;

import java.util.ArrayList;
import java.util.Collections;

/*
* https://programmers.co.kr/learn/courses/30/lessons/42861
*
* 최소 신장 트리 문제
* */
class Solution {

    static class Edge implements Comparable<Edge> {
        public int start;
        public int end;
        public int weight;

        public Edge(int start, int end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return weight - o.weight;
        }
    }

    private static int[] parent;

    public int solution(int n, int[][] costs) {
        int answer = 0;
        ArrayList<Edge> edges = new ArrayList<>();


        // make set
        parent = new int[n];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }

        for (int[] cost : costs) {
            edges.add(new Edge(cost[0], cost[1], cost[2]));
        }

        Collections.sort(edges);

        for (Edge edge : edges) {
            int startParent = find(edge.start);
            int endParent = find(edge.end);

            if (startParent != endParent) {
                union(edge.start, edge.end);
                answer += edge.weight;
            }
        }

        return answer;
    }

    private int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    private void union(int x, int y) {

        x = find(x);
        y = find(y);

        parent[y] = x;
    }
}

