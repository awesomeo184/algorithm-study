package study.recursivetreegraph;

public class Problem5 {

    public static int factorial(int n) {
        if (n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println(Problem5.factorial(5));
    }

}
