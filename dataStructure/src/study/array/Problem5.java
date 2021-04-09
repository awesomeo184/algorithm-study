package study.array;

/*
* 에라토스테네스의 체
* 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
*  만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.

* ▣ 입력설명
* 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

* ▣ 출력설명
* 첫 줄에 소수의 개수를 출력합니다.

* ▣ 입력예제 1
* 20

* ▣ 출력예제 1
*  8
* */

public class Problem5 {

    public int solution(int n) {
        int[] numbers = new int[n + 1];
        int count = 0;

        for (int i = 2; i <= n; i++) {
            if (numbers[i] == 0) {
                count++;
                for (int j = i; j <= n; j = j + i) {
                    numbers[j] = 1;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Problem5 p = new Problem5();

        int n = 20;

        System.out.println(p.solution(n));
    }

}
