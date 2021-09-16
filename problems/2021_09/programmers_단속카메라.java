/*
* https://programmers.co.kr/learn/courses/30/lessons/42884
*
* 구간 내에서 무조건 카메라 한 대를 마주쳐야 한다.
*
* 진출 시점을 기준으로 정렬하여, 진출 시점에 카메라를 그리디하게 배치한다.
*
* 현재 카메라의 위치가, 자동차의 진입위치보다 작다면 자동차의 진출 지점에 카메라를 설치한다.
* (자동차의 진출 지점을 기준으로 정렬했기 때문에, 다음 차의 진출 지점은 무조건 지금보다 같거나 크다, 따라서 자동차의 진출 지점에 카메라를 설치했을 때, 카메라의 위치 이전에 다음차가 진출할 일은 없다.)
*
* */
import java.util.Arrays;

class Solution {


    public int solution(int[][] routes) {
        int answer = 0;

        Arrays.sort(routes, (r1, r2) -> r1[1] - r2[1]);

        int camPosition = Integer.MIN_VALUE;

        for (int[] route : routes) {
            if (camPosition < route[0]) {
                camPosition = route[1];
                answer++;
            }
        }

        return answer;
    }
}
