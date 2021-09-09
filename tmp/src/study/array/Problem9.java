package study.array;

/*
* N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

* ▣ 입력설명
* 첫 줄에 자연수 N이 주어진다.(2<=N<=50)
* 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

* ▣ 출력설명
* 최대합을 출력합니다.

* ▣ 입력예제 1

* 5
* 10 13 10 12 15
* 12 39 30 23 11
* 11 25 50 53 15
* 19 27 29 37 27
* 19 13 30 13 19

* ▣ 출력예제 1
* 155
* */

public class Problem9 {

    public int solution(int[][] arr) {
        int max = 0;
        int cross1 = 0;
        int cross2 = 0;

        for (int i = 0; i < arr.length; i++) {
            int row = 0;
            int col = 0;
            for (int j = 0; j < arr.length; j++) {
                row += arr[i][j];
                col += arr[j][i];
                if (i == j) {
                    cross1 += arr[i][j];
                    cross2 += arr[i][arr.length - 1 - i];
                }
            }
            max = Math.max(max, row);
            max = Math.max(max, col);
        }

        max = Math.max(max, cross1);
        max = Math.max(max, cross2);


        return max;
    }

    public static void main(String[] args) {
        Problem9 p = new Problem9();

        int[][] arr = {{10, 13, 10, 12, 15},
            {12, 39, 30, 23, 11},
            {11, 25, 50, 53, 15},
            {19, 27, 29, 37, 27},
            {19, 13, 30, 13, 19}
        };

        System.out.println(p.solution(arr));
    }


}
