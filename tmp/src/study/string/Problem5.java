package study.string;

/*
 * 특정 문자 뒤집기
 * 영어 알파벳과 특수문자로 구성된 문자열이 주어지면 영어 알파벳만 뒤집고, 특수문자는 자기 자리에 그대로 있는 문자열을 만들어 출력하는 프로그램을 작성하세요.
 * ▣ 입력설명
 * 첫 줄에 길이가 100을 넘지 않는 문자열이 주어집니다.
 * ▣ 출력설명
 * 첫 줄에 알파벳만 뒤집힌 문자열을 출력합니다.
 * ▣ 입력예제 1 a#b!GE*T@S
 * ▣ 출력예제 1 S#T!EG*b@a
 */

public class Problem5 {

    public String solution(String str) {
        char[] chars = str.toCharArray();
        int lt = 0;
        int rt = str.length() - 1;

        while (lt < rt) {
            if (!Character.isAlphabetic(chars[lt])) {
                lt++;
            } else if (!Character.isAlphabetic(chars[rt])) {
                rt--;
            } else {
                char tmp = chars[lt];
                chars[lt] = chars[rt];
                chars[rt] = tmp;
                lt++;
                rt--;
            }
        }
        return String.valueOf(chars);
    }

    public static void main(String[] args) {
        Problem5 p = new Problem5();

        String str = "a@bc!T)e";

        System.out.println(p.solution(str));
    }

}
