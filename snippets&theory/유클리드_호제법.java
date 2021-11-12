// a > b
class Solution {
    int GCD_while(int a, int b){
        while(true){
            int r = a % b;

            if (r == 0) {
                return b;
            }

            a = b;
            b = r;
        }
    }

    int GCD_recursion(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return GCD_recursion(b, a % b);
        }
    }

    int LCM(int a, int b) {
        return a * b / GCD_while(a, b);
    }
}