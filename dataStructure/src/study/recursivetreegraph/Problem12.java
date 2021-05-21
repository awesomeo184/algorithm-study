package study.recursivetreegraph;

/*
 * 그래프 최단거리(BFS)
 *
 * 다음 그래프에서 1번 정점에서 각 정점으로 가는 최소 이동 간선수를 출력하세요.
 *
 * ▣ 입력설명
 * 첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연 결정보가 주어진다.
 *
 * ▣ 출력설명
 * 1번 정점에서 각 정점으로 가는 최소 간선수를 2번 정점부터 차례대로 출력하세요.
 *
 * ▣ 입력예제 1
 *
 * 6 9
 * 1 3
 * 1 4
 * 2 1
 * 2 5
 * 3 4
 * 4 5
 * 4 6
 * 6 2
 * 6 5
 *
 * ▣ 출력예제 1
 * 2:3
 * 3:1
 * 4:1
 * 5:2
 * 6:2
 * */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Problem12 {

    private static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    private static int[] visited;
    private static int[] distance;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numberOfVertexes = scanner.nextInt();
        int numberOfEdges = scanner.nextInt();

        visited = new int[numberOfVertexes + 1];
        distance = new int[numberOfVertexes + 1];
        for (int i = 0; i <= numberOfVertexes; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < numberOfEdges; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            graph.get(a).add(b);
        }

        BFS(1);

        for (int i = 2; i < distance.length; i++) {
            System.out.println(i + ": " + distance[i]);
        }
    }

    private static void BFS(int vertex) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(vertex);
        visited[vertex] = 1;

        while (!queue.isEmpty()) {
            Integer x = queue.poll();

            for (int nx : graph.get(x)) {
                if (visited[nx] == 0) {
                    visited[nx] = 1;
                    queue.add(nx);
                    distance[nx] = distance[x] + 1;
                }
            }
        }
    }
}
