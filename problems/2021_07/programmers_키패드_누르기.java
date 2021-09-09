// https://programmers.co.kr/learn/courses/30/lessons/67256

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    static class Position {

        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int calcDistance(Position other) {
            return Math.abs(this.x - other.x) + Math.abs(this.y - other.y);
        }
    }

    public static Map<Integer, Position> position = createMap();
    public static List<Integer> leftHandRange = Arrays.asList(1, 4, 7);
    public static List<Integer> rightHandRange = Arrays.asList(3, 6, 9);
    public String hand = "";
    public Position currentRightHandPosition = new Position(-1, 0);
    public Position currentLeftHandPosition = new Position(1, 0);


    public static Map<Integer, Position> createMap() {
        // 키패드 0을 영점으로 한 좌표 평면에서의 위치
        Map<Integer, Position> result = new HashMap<>();
        result.put(0, new Position(0, 0));
        result.put(1, new Position(-1, 3));
        result.put(2, new Position(0, 3));
        result.put(3, new Position(1, 3));
        result.put(4, new Position(-1, 2));
        result.put(5, new Position(0, 2));
        result.put(6, new Position(1, 2));
        result.put(7, new Position(-1, 1));
        result.put(8, new Position(0, 1));
        result.put(9, new Position(1, 1));
        return result;
    }

    public String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
        this.hand = hand.equals("left") ? "L" : "R";

        for (int number : numbers) {
            String thumb = getHand(number);
            sb.append(thumb);

            Position targetPosition = position.get(number);
            if (thumb.equals("R")) {
                this.currentRightHandPosition = targetPosition;
            } else {
                currentLeftHandPosition = targetPosition;
            }
        }

        return sb.toString();
    }

    public String getHand(int number) {
        if (leftHandRange.contains(number)) {
            return "L";
        }
        if (rightHandRange.contains(number)) {
            return "R";
        }

        Position targetPosition = Solution.position.get(number);
        int distanceFromRight = getDistance(targetPosition, currentRightHandPosition);
        int distanceFromLeft = getDistance(targetPosition, currentLeftHandPosition);
        if (distanceFromLeft < distanceFromRight) {
            return "L";
        } else if (distanceFromRight < distanceFromLeft) {
            return "R";
        }

        return this.hand;
    }

    public int getDistance(Position target, Position currentHandPosition) {
        return target.calcDistance(currentHandPosition);
    }
}
