/* 
* https://programmers.co.kr/learn/courses/30/lessons/42888?language=java
* 
* 해쉬를 이용하는 간단한 문제
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution {
        public String[] solution(String[] record) {
        ArrayList<String> arr = new ArrayList<>();

        Map<String, String> nicknameByUserId = new HashMap<>();

        for (int i = 0; i < record.length; i++) {
            String[] userInfo = record[i].split(" ");

            if (userInfo[0].equals("Enter") || userInfo[0].equals("Change")) {
                String userId = userInfo[1];
                String nickname = userInfo[2];
                nicknameByUserId.put(userId, nickname);
            }
        }

        for (String userInfo : record) {
            String[] tmp = userInfo.split(" ");

            String state = tmp[0];
            String userId = tmp[1];

            if (state.equals("Enter")) {
                arr.add(nicknameByUserId.get(userId) + "님이 들어왔습니다.");
            }
            if (state.equals("Leave")) {
                arr.add(nicknameByUserId.get(userId) + "님이 나갔습니다.");
            }
        }

        String[] answer = new String[arr.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = arr.get(i);
        }

        return answer;
    }
}
