# 선택 정렬 (Selection Sort)

## 특징

- 가장 기본적인 정렬 알고리즘이며 구현이 쉽다.
- 제자리 정렬 알고리즘이다.
- 불안정 정렬 알고리즘이다.
- 시간 복잡도가 O(n**2)으로 상당히 느리다.

## 기본 아이디어

- 배열을 순회하며 최소값을 찾는다. 최소값을 찾으면 배열의 가장 첫 인덱스에 있는 값과 자리를 바꾼다. (최대값을 찾을 수도 있다. 이때는 가장 뒤에 있는 값과 자리를 바꾼다.)
- 다시 배열을 순회하며 다음 최소값을 찾는다. 최소값을 찾으면 두 번째 인덱스에 있는 값과 자리를 바꾼다.
- 원소가 하나 남을 때까지 위 과정을 반복한다.

원소가 들어갈 자리는 이미 정해져 있고, 그 자리에 넣을 원소를 **선택**하는 알고리즘

![Selection-Sort-Gif](https://user-images.githubusercontent.com/63030569/111444069-58624980-874d-11eb-82a0-90643cbc6dfc.gif)

## 의사코드

```
Algorithm selection_sort(array)
    input: array
    output: sorted array

    for i = 1 to length of array - 1 do   // for-loop를 n-1회 반복
        min_index = find_min_index(array, i)
        swap(min_index, i)
    return array

Algorithm find_min_index(array, i)
    input: array, index to start
    output: index of minimum element
    
    min_index = i 
    min_element = array[i]
    
    for j = i+1 to length of array do  // for-loop를 n-i회 반복
        if (array[j] < min_element) then
            min_index = j
            min_element = array[j]
    return min_index

Algorithm swap(min_index, i)
    input: index of minimum element, index to be replaced
    output: void
    
    tmp = array[i]
    array[i] = array[min_index]
    array[min_index] = tmp
```

## 시간 복잡도 분석

### 비교 연산

외부 루프 (n-1회 반복)

1회차: 내부루프 n - 1회 반복

2회차: 내부루프 n - 2회 반복

3회차: 내부루프 n - 3회 반복

...

n-1회차: 내부루프 1회 반복

총 비교연산 횟수: 1 + 2 + 3 + ... + n-1 = n(n-1)/2

총 시간 복잡도는 n(n-1)/2 -> O(n**2)
스왑할 때 일어나는 할당 연산은 O(n) 이므로 무시


## 파이썬 코드

```python
from typing import List

def find_min_index(array: List, i: int) -> int:
    min_index: int = i
    min_element: int = array[i]

    for j in range(i + 1, len(array)):
        if array[j] < min_element:
            min_index = j
            min_element = array[j]

    return min_index


def selection_sort(array: List) -> List:
    for i in range(len(array) - 1):
        min_index: int = find_min_index(array, i)

        tmp: int = array[i]
        array[i]: int = array[min_index]
        array[min_index]: int = tmp

    return array
```