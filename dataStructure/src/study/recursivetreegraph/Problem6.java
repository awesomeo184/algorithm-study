package study.recursivetreegraph;

public class Problem6 {

    public static int fibo(int n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return 1;
        }
        return fibo(n - 2) + fibo(n - 1);
    }

    public static void main(String[] args) {
        int n = 10;

        for (int i = 0; i < n; i++) {
            System.out.print(fibo(i) + " ");
        }

    }

}
