/*
* https://www.acmicpc.net/problem/2178
*
* 미로탐색
*
* BFS로 탐색할 경우, 목표지점에 가장 처음 도달하는 경우가 최단경로. 이후에 값을 못바꾸도록 처리만 해주면 최단 거리를 유지할 수 있다.
*
* */


import java.util.LinkedList;
import java.util.Scanner;

public class Main {

    private static int N;
    private static int M;
    private static int[][] maze;

    // 상하좌우
    private static int[] dx = new int[]{0, 0, -1, 1};
    private static int[] dy = new int[]{-1, 1, 0, 0};

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();

        maze = new int[N][M];

        for (int i = 0; i < N; i++) {
            String seq = sc.nextLine();
            for (int j = 0; j < M; j++) {
                maze[i][j] = seq.charAt(j) - '0';
            }
        }

        BFS(0, 0);
        System.out.println(maze[N-1][M-1]);
    }

    private static void BFS(int row, int col) {

        LinkedList<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int curY = poll[0];
            int curX = poll[1];

            for (int i = 0; i < 4; i++) {
                int ny = curY + dy[i];
                int nx = curX + dx[i];

                if (0 <= ny && ny < N && 0 <= nx && nx < M) {
                    if (maze[ny][nx] == 1) {
                        queue.add(new int[]{ny, nx});
                        maze[ny][nx] = maze[curY][curX] + 1;
                    }
                }
            }
        }
    }
}
