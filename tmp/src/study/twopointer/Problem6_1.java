package study.twopointer;

public class Problem6_1 {

    public int solution(int k, int[] arr) {
        int answer =0;
        int count = 0;
        int lt = 0;

        for (int rt = 0; rt < arr.length; rt++) {
            if (arr[rt] == 0) {
                count++;
            }
            while (count > k) {
                if (arr[lt] == 0) {
                    count--;
                }
                lt++;
            }
            answer = Math.max(answer, rt - lt + 1);
        }

        return answer;
    }

        public static void main(String[] args) {
        Problem6_1 p = new Problem6_1();

        int k = 2;
        int[] arr = {1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1};

        System.out.println(p.solution(k, arr));
    }

}
