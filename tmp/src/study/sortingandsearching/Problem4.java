package study.sortingandsearching;

/*
* LRU
* ▣ 입력설명
* 첫 번째 줄에 캐시의 크기인 S(3<=S<=10)와 작업의 개수 N(5<=N<=1,000)이 입력된다. 두 번째 줄에 N개의 작업번호가 처리순으로 주어진다. 작업번호는 1 ~100 이다.
* ▣ 출력설명
* 마지막 작업 후 캐시메모리의 상태를 가장 최근 사용된 작업부터 차례로 출력합니다.
* ▣ 입력예제 1
* 59
* 123262357
* ▣ 출력예제 1
* 75326
*
* */

import java.util.Arrays;

public class Problem4 {

    public static int[] solution(int size, int n, int[] arr) {
        int[] cache=new int[size];
        for(int x : arr){
            int pos=-1;
            for(int i=0; i<size; i++) if(x==cache[i]) pos=i;
            if(pos==-1){
                for(int i=size-1; i>=1; i--){
                    cache[i]=cache[i-1];
                }
            }
            else{
                for(int i=pos; i>=1; i--){
                    cache[i]=cache[i-1];
                }
            }
            cache[0]=x;
        }
        return cache;
    }

    public static void main(String[] args) {
        int S = 5;
        int N = 9;
        int[] arr = {1, 2, 3, 2, 6, 2, 3, 5, 7};

        int[] answer = Problem4.solution(S, N, arr);
        System.out.println(Arrays.toString(answer));
    }

}
