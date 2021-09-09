package study.sortingandsearching;

/*
* 삽입정렬
* N개이 숫자가 입력되면 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요. 정렬하는 방법은 삽입정렬입니다.
* ▣ 입력설명
* 첫 번째 줄에 자연수 N(1<=N<=100)이 주어집니다.
* 두 번째 줄에 N개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 정수형 범위 안에 있습니다.
* ▣ 출력설명
* 오름차순으로 정렬된 수열을 출력합니다.
* ▣ 입력예제 1 6
* 11 7 5 6 10 9
* ▣ 출력예제 1 5 6 7 9 10 11
* */

import java.util.Arrays;

public class Problem3 {

    public static void main(String[] args) {
        int[] arr = {11, 7, 5, 6, 10, 9};

        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];

            int j = i -1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }

        System.out.println(Arrays.toString(arr));
    }
}
