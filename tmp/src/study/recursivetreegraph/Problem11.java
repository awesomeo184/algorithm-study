package study.recursivetreegraph;

/*
* 경로탐색(인접리스트)
* */

import java.util.ArrayList;
import java.util.Arrays;

public class Problem11 {
    private static int n;
    private static int answer = 0;

    private static int[] visited;
    private static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) {
        graph = new ArrayList<>();

        graph.add(new ArrayList<>(Arrays.asList()));
        graph.add(new ArrayList<>(Arrays.asList(2,3,4)));
        graph.add(new ArrayList<>(Arrays.asList(1,3,5)));
        graph.add(new ArrayList<>(Arrays.asList(4)));
        graph.add(new ArrayList<>(Arrays.asList(2,5)));
        graph.add(new ArrayList<>(Arrays.asList()));

        n = 5;
        visited = new int[n+1];

        visited[1] = 1;
        DFS(1);
        System.out.println(answer);
    }

    private static void DFS(int vertex) {
        if (vertex == n) {
            answer++;
        } else {
            for (int i : graph.get(vertex)) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    DFS(i);
                    visited[i] = 0;
                }
            }
        }
    }
}
