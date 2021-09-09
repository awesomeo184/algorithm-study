import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();

        int idx = 0;
        boolean isFirstAlphabet = true;
        while (idx < s.length()) {
            if (s.charAt(idx) == ' ') {
                isFirstAlphabet = true;
                sb.append(' ');
                idx++;
                continue;
            }

            if (isFirstAlphabet) {
                sb.append(Character.toUpperCase(s.charAt(idx)));
                isFirstAlphabet = false;
            } else {
                sb.append(Character.toLowerCase(s.charAt(idx)));
            }
            idx++;
        }

        return sb.toString();
    }

}