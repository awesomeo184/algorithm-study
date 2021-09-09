/* 
* https://programmers.co.kr/learn/courses/30/lessons/42576
* 완주하지 못한 선수는 무조건 한 명이므로 이름 순으로 정렬해서 completion에 포함되어 있지 않으면 답을 리턴
* 정렬을 한번 하고 배열을 순회하므로 시간 복잡도는 O(NlogN)
* 문제 분류는 해시인데, 해시맵에 Map<String, Count> 형태로 담은 후 participant를 담을 때는 카운트를 올리고,
* 다시 completion을 돌면서 카운트를 줄인 뒤, 카운트가 여전히 남아있는 이름을 반환하면 O(N)에 풀이 가능할듯
*/

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                answer = participant[i];
            }
        }
        if (answer.equals("")) {
            answer = participant[participant.length - 1];
        }
        return answer;
    }
}