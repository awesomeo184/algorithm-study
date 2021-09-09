# 버블 정렬 (Bubble Sort)

## 특징
- 구현이 쉽다.
- 제자리 정렬이다.
- 안정 정렬이다.
- 시간 복잡도가 O(n^2)으로 느리다.
- 스왑 연산이 많이 일어나기 때문에 굉장히 비효율적이다.

## 기본 아이디어
배열을 순회하면서 서로 인접한 두 원소를 비교한다. 만약 더 큰 원소가 앞쪽에 있다면 두 원소의 자리를 바꾼다(오름차순 기준).

![bubblesort](https://user-images.githubusercontent.com/63030569/111561372-af146580-87d7-11eb-97ce-99ffbc5283a5.gif)

만약 마지막까지 도달했는데 스왑이 한번도 일어나지 않았다면, 모든 원소가 정렬 상태에 도달한 것으로 판단할 수 있다.
이때는 연산이 끝나지 않았음에도 강제로 연산을 종료함으로써 수행시간을 조금 더 줄일 수 있다.

## 의사코드

```HTML
Algorithm bubble_sort(array)
    input: array
    output: void

    n = length of array

    for i = n-1 to 2 by -1 do
        sorted = True           // 정렬되어있는 상태인지
        sort(array, i, sorted)
        if sorted then
            break

Algorithm sort(array, i, sorted)
    input: array, index for terminating loop, flag
    output: void

    for j = 1 to i do
        if array[j] > array[j+1] then
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1] = tmp
            sorted = False     // 정렬되어있지 않았음

```
