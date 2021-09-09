package study.twopointer;


import java.util.ArrayList;

/*
* 오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램 을 작성하세요.
* ▣ 입력설명
* 첫 번째 줄에 첫 번째 배열의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 배열 원소가 오름차순으로 주어집니다.
* 세 번째 줄에 두 번째 배열의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 배열 원소가 오름차순으로 주어집니다.
* 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

* ▣ 출력설명
* 오름차순으로 정렬된 배열을 출력합니다.
*
* ▣ 입력예제 1
* 3
* 1 3 5
* 5
* 2 3 6 7 9
* ▣ 출력예제 1
* 1 2 3 3 5 6 7 9
* */
public class Problem1 {

    public ArrayList<Integer> solution(int[] a, int[] b) {
        ArrayList<Integer> answer = new ArrayList<>();

        int p1 = 0, p2 = 0;
        while (p1 < a.length && p2 < b.length) {
            if (a[p1] < b[p2]) {
                answer.add(a[p1++]);
            } else {
                answer.add(b[p2++]);
            }
        }

        while (p1 < a.length) {
            answer.add(a[p1++]);
        }
        while (p2 < b.length) {
            answer.add(b[p2++]);
        }

        return answer;
    }

    public static void main(String[] args) {
        Problem1 p = new Problem1();

        int[] a = {1, 3, 5};
        int[] b = {2, 3, 6, 7, 9};

        ArrayList<Integer> answer = p.solution(a, b);

        for (Integer integer : answer) {
            System.out.print(integer + " ");
        }
    }
}
