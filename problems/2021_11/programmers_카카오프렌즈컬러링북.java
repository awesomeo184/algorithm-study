/*
 https://programmers.co.kr/learn/courses/30/lessons/1829?language=java
 */

import java.util.*;

class Solution {
    private static int[] dx = new int[]{0, 0, -1, 1};
    private static int[] dy = new int[]{-1, 1, 0, 0};

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {

                    Queue<int[]> queue = new LinkedList<>();
                    int color = picture[i][j];
                    int sizeOfArea = 1;
                    visited[i][j] = true;
                    numberOfArea++;

                    queue.add(new int[]{i, j});
                    while (!queue.isEmpty()) {
                        int[] xy = queue.poll();
                        for (int k = 0; k < 4; k++) {
                            int nx = xy[0] + dx[k];
                            int ny = xy[1] + dy[k];
                            if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny]
                                && picture[nx][ny] == color) {
                                visited[nx][ny] = true;
                                queue.add(new int[]{nx, ny});
                                sizeOfArea++;
                            }
                        }
                    }
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, sizeOfArea);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}