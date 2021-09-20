
/*
* https://programmers.co.kr/learn/courses/30/lessons/83201
* N * N 배열에서 컬럼에 대한 값을 계산, min, max를 구하는 기본적인 알고리즘 이용
* */

class Solution {
    public String solution(int[][] scores) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < scores.length; i++) {

            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            boolean isUnique = true;
            int length = scores.length;
            int sum = 0;
            int selfScored = scores[i][i];

            for (int j = 0; j < length; j++) {
                min = Math.min(scores[j][i], min);
                max = Math.max(scores[j][i], max);
                if (i != j && selfScored == scores[j][i]) {
                    isUnique = false;
                }
                sum += scores[j][i];
            }

            if (isUnique && (min == selfScored || max == selfScored)) {
                length -= 1;
                sum -= selfScored;
            }
            sb.append(scoreToGrade(sum / length));
        }

        return sb.toString();
    }

    private char scoreToGrade(int avg) {
        if (avg >= 90) {
            return 'A';
        } else if (avg >= 80) {
            return 'B';
        } else if (avg >= 70) {
            return 'C';
        } else if (avg >= 50) {
            return 'D';
        }
        return 'F';
    }
}

