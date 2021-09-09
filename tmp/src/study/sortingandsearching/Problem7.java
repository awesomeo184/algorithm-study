package study.sortingandsearching;

import java.util.ArrayList;
import java.util.Collections;

/*
* 좌표정렬
* N개의 평면상의 좌표(x, y)가 주어지면 모든 좌표를 오름차순으로 정렬하는 프로그램을 작성하 세요. 정렬기준은 먼저 x값의 의해서 정렬하고, x값이 같을 경우 y값에 의해 정렬합니다.
* ▣ 입력설명
* 첫째 줄에 좌표의 개수인 N(3<=N<=100,000)이 주어집니다.
* 두 번째 줄부터 N개의 좌표가 x, y 순으로 주어집니다. x, y값은 양수만 입력됩니다.
*
* ▣ 출력설명
* N개의 좌표를 정렬하여 출력하세요.
*
* ▣ 입력예제 1
* 5
* 2 7
* 1 3
* 1 2
* 2 5
* 3 6
*
* ▣ 출력예제 1
* 12
* 1 3
* 2 5
* 2 7
* 3 6
* */
public class Problem7 {

    public static void solution(int[][] arr) {
        ArrayList<Point> points = new ArrayList<>();
        for (int[] p : arr) {
            points.add(new Point(p[0], p[1]));
        }
        Collections.sort(points);

        for (Point p : points) {
            System.out.println(p.x + " " + p.y);
        }
    }

    public static void main(String[] args) {
        int[][] arr = {
            {2, 7},
            {1, 3},
            {1, 2},
            {2, 5},
            {3, 6},
        };

        Problem7.solution(arr);
    }
}

class Point implements Comparable<Point> {

    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point other) {
        if (this.x == other.x) {
            return this.y - other.y;
        }
        return this.x - other.y;
    }
}
