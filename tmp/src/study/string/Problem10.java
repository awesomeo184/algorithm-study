package study.string;

/*
* 가장 짧은 문자 거리
* 한 개의 문자열 s와 문자 t가 주어지면 문자열 s의 각 문자가 문자 t와 떨어진 최소거리를 출 력하는 프로그램을 작성하세요.
* ▣ 입력설명
* 첫 번째 줄에 문자열 s와 문자 t가 주어진다. 문자열과 문자는 소문자로만 주어집니다. 문자열의 길이는 100을 넘지 않는다.
* ▣ 출력설명
* 첫 번째 줄에 각 문자열 s의 각 문자가 문자 t와 떨어진 거리를 순서대로 출력한다.
* ▣ 입력예제 1 teachermode e
* ▣ 출력예제 1 10121012210
*/


import java.util.Arrays;

public class Problem10 {

    public static void main(String[] args) {
        Problem10 p = new Problem10();

        String str = "teachermode";
        char c = 'e';

        System.out.println(Arrays.toString(p.solution(str, c)));
    }

    private int[] solution(String str, char c) {
        int[] answer = new int[str.length()];

        int p = 1000;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == c) {
                p = 0;
                answer[i] = p;
            } else {
                p++;
                answer[i] = p;
            }
        }

        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == c) {
                p = 0;
            } else {
                p++;
                answer[i] = Math.min(answer[i], p);
            }
        }

        return answer;
    }

}
