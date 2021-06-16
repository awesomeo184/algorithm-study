package study.graph.dijkstra;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

/*
 *  다익스트라 알고리즘
 * 아래의 가중치 방향그래프에서 1번 정점에서 모든 정점으로의 최소 거리비용을 출력하는 프로 그램을 작성하세요.(경로가 없으면 Impossible를 출력한다)
 * */
public class Main {

    public static int[] distance;
    public static ArrayList<ArrayList<Edge>> graph = new ArrayList<>();


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfVertex = scanner.nextInt();
        int numberOfEdge = scanner.nextInt();

        for (int i = 0; i <= numberOfVertex; i++) {
            graph.add(new ArrayList<Edge>());
        }

        distance = new int[numberOfVertex + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        for (int i = 0; i < numberOfEdge; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            graph.get(a).add(new Edge(b, c));
        }

        solution(1);

        for(int i=2; i<=numberOfVertex; i++){
            if(distance[i]!=Integer.MAX_VALUE) System.out.println(i+" : "+distance[i]);
            else System.out.println(i+" : impossible");
        }

    }

    public static void solution(int start) {
        PriorityQueue<Edge> minHeap = new PriorityQueue<>();

        minHeap.offer(new Edge(start, 0));

        while (!minHeap.isEmpty()) {
            Edge tmp = minHeap.poll();

            int now = tmp.vertex;
            int nowDistance = tmp.distance;

            // 현재 계산된 거리가 최단경로일 가능성이 없다면
            if (nowDistance > distance[now]) {
                continue;
            }

            for (Edge e : graph.get(now)) {
                if (distance[e.vertex] > nowDistance + e.distance) {
                    distance[e.vertex] = nowDistance + e.distance;
                    minHeap.offer(new Edge(e.vertex, distance[e.vertex]));
                }
            }


        }

    }
}

class Edge implements Comparable<Edge> {

    int vertex;
    int distance;

    public Edge(int vertex, int distance) {
        this.vertex = vertex;
        this.distance = distance;
    }

    @Override
    public int compareTo(Edge other) {
        return this.distance - other.distance;
    }
}

