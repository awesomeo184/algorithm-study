package study.recursivetreegraph;

/*
* 송아지 찾기(BFS 상태트리 탐색)
*
* 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아 지의 위치가 수직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음 과 같은 방법으로 이동한다. 송아지는 움직이지 않고 제자리에 있다.
* 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성 하세요.
* ▣ 입력설명
* 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.
* ▣ 출력설명
* 점프의 최소횟수를 구한다. 답은 1이상입니다.
* ▣ 입력예제 1
* 5 14
* ▣ 출력예제 1
* 3
* ▣ 입력예제 2
* 8 3
* ▣ 출력예제 2
* 5
* */

import java.util.LinkedList;
import java.util.Queue;

public class Problem9 {

    private static int answer = 0;
    private static int[] dx = {-1, 1, 5};
    private static int[] visited = new int[10001];
    private static int[] level = new int[10001];

    public static void main(String[] args) {
        int start = 8;
        int end = 3;

        System.out.println(solution(start, end));
    }

    private static int solution(int start, int end) {
        BFS(start, end);
        return answer;
    }

    private static void BFS(int start, int end) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            visited[vertex] = 1;

            for (int i = 0; i < 3; i++) {
                int x = dx[i];
                int nextVertex = vertex + x;

                if (nextVertex == end) {
                    answer = level[vertex] + 1;
                    return;
                }

                // 방문처리, 범위 처리
                if (nextVertex >= 1 && nextVertex < 10001 && visited[nextVertex] == 0) {
                    queue.add(nextVertex);
                    level[nextVertex] = level[vertex] + 1;
                }

            }

        }
    }
}
