/*
 * https://programmers.co.kr/learn/courses/30/lessons/1835?language=java
 * 순열 구하기
 */

import java.util.*;

class Solution {

    public int solution(int n, String[] data) {

        int count = 0;

        List<Character> origins = new ArrayList<>(List.of('A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'));
        List<List<Character>> permutations = getPermutations(origins);

        for (List<Character> permutation : permutations) {
            if (checkCoundition(permutation, data)) {
                count++;
            }
        }
        return count;
    }

    private List<List<Character>> getPermutations(List<Character> origins) {

        if (origins.isEmpty()) {
            List<List<Character>> result = new ArrayList<>();
            result.add(new ArrayList<>());
            return result;
        }

        Character firstElem = origins.remove(0);
        List<List<Character>> returnValue = new ArrayList<>();
        List<List<Character>> permutation = getPermutations(origins);
        for (List<Character> smallPermutation : permutation) {
            for (int i = 0; i <= smallPermutation.size(); i++) {
                List<Character> temp = new ArrayList<>(smallPermutation);
                temp.add(i, firstElem);
                returnValue.add(temp);
            }
        }
        return returnValue;
    }

    private boolean checkCoundition(List<Character> permutation, String[] data) {

        for (String datum : data) {
            char first = datum.charAt(0);
            char second = datum.charAt(2);
            char symbol = datum.charAt(3);
            int number = datum.charAt(4) - '0';
            int indexDiff = Math.abs(permutation.indexOf(first) - permutation.indexOf(second));

            if (symbol == '=') {
                if (!(indexDiff == number + 1)) {
                    return false;
                }
            }

            if (symbol == '>') {
                if (!(indexDiff > number + 1)){
                    return false;
                }
            }

            if (symbol == '<') {
                if (!(indexDiff < number + 1)){
                    return false;
                }
            }
        }
        return true;
    }
}