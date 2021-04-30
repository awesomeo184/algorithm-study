package study.recursivetreegraph;

public class Problem2 {

    public static void binary(int n) {
        if (n / 2 == 0) {
            System.out.print(n % 2);
            return;
        }
        binary(n / 2);
        System.out.print(n % 2);
    }

    public static void main(String[] args) {
        Problem2.binary(11);
    }

}
