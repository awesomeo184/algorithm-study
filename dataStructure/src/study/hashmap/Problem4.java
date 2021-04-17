package study.hashmap;

/*
* S문자열에서 T문자열과 아나그램이 되는 S의 부분문자열의 개수를 구하는 프로그램을 작성하 세요. 아나그램 판별시 대소문자가 구분됩니다. 부분문자열은 연속된 문자열이어야 합니다.
* ▣ 입력설명
* 첫 줄에 첫 번째 S문자열이 입력되고, 두 번째 줄에 T문자열이 입력됩니다.
* S문자열의 길이는 10,000을 넘지 않으며, T문자열은 S문자열보다 길이가 작거나 같습니다.
* ▣ 출력설명
* S단어에 T문자열과 아나그램이 되는 부분문자열의 개수를 출력합니다.
* ▣ 입력예제 1
* bacaAacba
* abc
* ▣ 출력예제 1
* 3
* 출력설명: {bac}, {acb}, {cba} 3개의 부분문자열이 "abc"문자열과 아나그램입니다.
*
* ▣ 입력예제 2
* bacaAacbaa
* abca
* ▣ 출력예제 2
* 3
* */

import java.util.HashMap;

public class Problem4 {

    public int solution(String seq, String sub) {
        int answer = 0;
        HashMap<Character, Integer> subMap = new HashMap<>();
        HashMap<Character, Integer> seqMap = new HashMap<>();

        for (char c : sub.toCharArray()) {
            subMap.put(c, subMap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < sub.length() - 1; i++) {
            seqMap.put(seq.charAt(i), seqMap.getOrDefault(seq.charAt(i), 0) + 1);
        }

        int lt= 0;
        for (int rt = sub.length() - 1; rt < seq.length(); rt++) {
            seqMap.put(seq.charAt(rt), seqMap.getOrDefault(seq.charAt(rt), 0) + 1);
            if (subMap.equals(seqMap)) {
                answer++;
            }

            char charAtLt = seq.charAt(lt);
            seqMap.put(charAtLt, seqMap.get(charAtLt) - 1);
            if (seqMap.get(charAtLt) == 0) {
                seqMap.remove(charAtLt);
            }
            lt++;
        }

        return answer;
    }

    public static void main(String[] args) {
        Problem4 p = new Problem4();

        String seq = "bacaAacbaa";
        String sub = "abca";

        System.out.println(p.solution(seq, sub));
    }
}
