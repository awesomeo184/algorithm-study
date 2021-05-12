package study.recursivetreegraph;

public class Problem6 {

    public static int[] dp;

    public static int fibo(int n) {

        if (dp[n] != 0) {
            return dp[n];
        } else {
            dp[n] = fibo(n - 2) + fibo(n - 1);
            return dp[n];
        }
    }

    public static void main(String[] args) {
        int n = 10;

        dp = new int[n];

        if (n >= 0) {
            dp[0] = 1;
            dp[1] = 1;
        }
        fibo(n-1);

        for (int i : dp) {
            System.out.print(i + " ");
        }
    }

}
