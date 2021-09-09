package study.twopointer;

public class Problem5_1 {

    public static void main(String[] args) {
        Problem5_1 p = new Problem5_1();

        int n = 15;

        System.out.println(p.solution(n));
    }

    public int solution(int n) {
        int answer = 0;
        int count = 1;
        n--;
        while (n > 0) {
            count++;
            n = n - count;
            if (n % count == 0) {
                answer++;
            }
        }
        return answer;
    }

}
