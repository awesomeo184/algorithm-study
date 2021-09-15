/*
* https://www.acmicpc.net/problem/1260
* 
* DFS와 BFS
* 
* DFS, BFS 기초
* 
* */

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

    private static int[][] graph;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int V = sc.nextInt();
        int E = sc.nextInt();
        int start = sc.nextInt();

        graph = new int[V + 1][V + 1];
        boolean[] visited = new boolean[V + 1];

        for (int i = 0; i < E; i++) {
            int head = sc.nextInt();
            int tail = sc.nextInt();

            graph[head][tail] = 1;
            graph[tail][head] = 1;
        }

        DFS(start, visited);
        System.out.println();
        Arrays.fill(visited, false);
        BFS(start, visited);
    }

    private static void DFS(int start, boolean[] visited) {

        System.out.print(start + " ");
        visited[start] = true;
        for (int i = 1; i < graph.length; i++) {
            if (graph[start][i] == 1 && !visited[i]) {
                DFS(i, visited);
            }
        }
    }

    private static void BFS(int start, boolean[] visited) {

        LinkedList<Integer> queue = new LinkedList<>();

        queue.add(start);
        visited[start] = true;
        while (!queue.isEmpty()) {
            Integer poll = queue.poll();
            System.out.print(poll + " ");

            for (int i = 1; i < graph.length; i++) {
                if (graph[poll][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }

}

