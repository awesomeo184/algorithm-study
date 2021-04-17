package study.stack;

import java.util.Stack;

/*
* 괄호문자 제거
* 입력된 문자열에서 소괄호 ( ) 사이에 존재하는 모든 문자를 제거하고 남은 문자만 출력하는 프로그램을 작성하세요.
* ▣ 입력설명
* 첫 줄에 문자열이 주어진다. 문자열의 길이는 100을 넘지 않는다.
* ▣ 출력설명
* 남은 문자만 출력한다.
* ▣ 입력예제 1
* (A(BC)D)EF(G(H)(IJ)K)LM(N)
* ▣ 출력예제 1
* EFLM
* */

public class Problem2 {

    public String solution(String str) {
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for (char x : str.toCharArray()) {
            if (x == ')') {
                while (stack.pop() != '(') { }
            } else {
                stack.push(x);
            }
        }
        for(int i=0; i<stack.size(); i++) answer+=stack.get(i);
        return answer;
    }

    public static void main(String[] args) {
        Problem2 p = new Problem2();

        String str = "(A(BC)D)EF(G(H)(IJ)K)LM(N)";

        System.out.println(p.solution(str));
    }

}
