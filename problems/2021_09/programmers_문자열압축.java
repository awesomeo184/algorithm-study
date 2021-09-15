/*
* https://programmers.co.kr/learn/courses/30/lessons/60057
*
* 가장 짧게 압축되는 경우 찾기
*
* brute force

* for k=1 to str.length:
*   k개만큼 문자열을 자른다.
*   이전것과 비교해서 같으면 count 1 증가
*   최솟값 갱신
*
* */

public class Solution {

    public int solution(String s) {
        int min = Integer.MAX_VALUE;

        if (s.length() <= 1) {
            return s.length();
        }

        for (int i = 1; i < s.length(); i++) {
            int count = 1;
            StringBuilder compressed = new StringBuilder();
            String prev = s.substring(0, i);
            for (int j = i; j < s.length(); j = j + i) {
                // end index가 범위 벗어나는 경우 예외처리
                String substring;
                if (j + i >= s.length()) {
                    substring = s.substring(j);
                } else {
                    substring = s.substring(j , j + i);
                }

                if (substring.equals(prev)) {
                    count++;
                } else {

                    if (count <= 1) {
                        compressed.append(prev);
                    } else {
                        compressed.append(count).append(prev);
                    }
                    count = 1;
                }
                prev = substring;
            }

            // 마지막 문자 처리
            if (count <= 1) {
                compressed.append(prev);
            } else {
                compressed.append(count).append(prev);
            }

            min = Math.min(min, compressed.length());
        }

        return min;
    }
}
