package study.stack;

import java.util.Stack;

/*
* 쇠막대기
* ▣ 입력설명
* 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.
* ▣ 출력설명
* 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
* ▣ 입력예제 1
* ()(((()())(())()))(())
* ▣ 출력예제 1
* 17
* ▣ 입력예제 2
* (((()(()()))(())()))(()())
* ▣ 출력예제 2
* 24
* */
public class Problem5 {

    public static int solution(String input) {
        int answer = 0;
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else {
//                만약 레이저라면
                stack.pop();
                if (input.charAt(i - 1) == '(') {
                    answer += stack.size();
                } else {
                    answer++;
                }
            }
        }
        return answer;
    }


    public static void main(String[] args) {
        String input = "()(((()())(())()))(())";
        System.out.println(Problem5.solution(input));
    }
}
