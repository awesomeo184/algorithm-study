package study.DFSandBFS;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Problem3 {

    private static int n;
    private static int timeLimit;
    private static int totalScore;
    private static List<Problem> problems;



    static class Problem {
        private int score;
        private int cost;

        public Problem(int score, int cost) {
            this.score = score;
            this.cost = cost;
        }

        public int getScore() {
            return score;
        }

        public int getCost() {
            return cost;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        timeLimit = scanner.nextInt();
        problems = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int score = scanner.nextInt();
            int cost = scanner.nextInt();

            problems.add(new Problem(score, cost));
        }

        DFS(0, 0, 0);
        System.out.println(totalScore);
    }

    private static void DFS(int level, int score, int cost) {
        if (cost > timeLimit) {
            return;
        }

        if (level == n) {
            totalScore = Math.max(totalScore, score);
        } else {
            DFS(level + 1,
                score + problems.get(level).getScore(),
                cost + problems.get(level).getCost()
            );

            DFS(level + 1,
                score,
                cost
            );
        }
    }

}
