package study.recursivetreegraph;

public class Problem1 {

    public static void count(int n) {
        if (n == 1) {
            System.out.print(n + " ");
            return;
        }
        count(n-1);
        System.out.print(n + " ");
    }

    public static void main(String[] args) {
        Problem1.count(3);
    }

}
