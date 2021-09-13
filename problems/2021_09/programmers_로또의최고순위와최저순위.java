/*
 * https://programmers.co.kr/learn/courses/30/lessons/77484
 * 단순한 탐색문제
 * lottos에서 0의 개수를 센다.
 * lottos와 win_nums를 비교해서 같은 숫자가 있으면 count를 증가
 *
 * worst -> 0을 답으로 포함하지 않는 경우
 * best -> 0을 답으로 포함하는 경우
 *
 * 입력 배열의 크기가 6개로 정해져있기 때문에 nested for-loop를 이용하는 것이 더 빠르다.
 * 입력 배열의 크기가 크다면 Set을 이용하는 것이 더 빠르다. HashSet.contains() 메서드는 상수 시간의 복잡도를 갖는다.
 * */

import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {

    public int[] solutionBySet(int[] lottos, int[] win_nums) {
        int matchedCount = 0;
        int zeroCount = 0;

        Set<Integer> winNumsSet = Arrays.stream(win_nums).boxed().collect(Collectors.toSet());

        for (int lotto : lottos) {
            if (lotto == 0) {
                zeroCount++;
                continue;
            }
            if (winNumsSet.contains(lotto)) {
                matchedCount++;
            }
        }

        int worst = getRank(matchedCount);
        int best = getRank(matchedCount + zeroCount);

        return new int[]{best, worst};
    }

    public int[] solutionByNestedForLoop(int[] lottos, int[] win_nums) {
        int[] answer = {};

        int count = 0;
        int zeroCount = 0;

        for (int i = 0; i < lottos.length; i++) {
            int lotto = lottos[i];
            if (lotto == 0) {
                zeroCount++;
                continue;
            }

            for (int j = 0; j < win_nums.length; j++) {
                int win_num = win_nums[j];
                if (lotto == win_num) {
                    count++;
                }
            }
        }

        int worst = getRank(count);
        int best = getRank(count + zeroCount);

        return new int[]{best, worst};
    }

    private int getRank(int count) {
        int rank = 7 - count;
        return Math.min(rank, 6);
    }
}
