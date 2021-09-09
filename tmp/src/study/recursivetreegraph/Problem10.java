package study.recursivetreegraph;


/*
* 경로 탐색 (인접 행렬)
*
* 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프 로그램을 작성하세요.
* ▣ 입력설명
* 첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연 결정보가 주어진다.
* ▣ 출력설명
* 총 가지수를 출력한다.
* ▣ 입력예제 1
* 5 9
* 1 2
* 1 3
* 1 4
* 2 1
* 2 3
* 2 5
* 3 4
* 4 2
* 4 5
* ▣ 출력예제 1
* 6
 * */
public class Problem10 {
    private static int n;
    private static int[][] graph;
    private static int[] visited;
    private static int answer = 0;

    public static void main(String[] args) {
        n = 5;

        graph = new int[][] {
            {0, 1, 1, 1, 0},
            {1, 0, 1, 0, 1},
            {0, 0, 0, 1, 0},
            {0, 1, 0, 0, 1},
            {0, 0, 0, 0, 0}
        };

        visited = new int[n];
        visited[0] = 1;
        DFS(0);
        System.out.println(answer);

    }

    private static void DFS(int vertex) {
        if (vertex == n-1) {
            answer++;
        }
        else {
            for (int i = 0; i < n; i++) {
                if (graph[vertex][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    DFS(i);
                    visited[i] = 0;
                }
            }
        }
    }
}
