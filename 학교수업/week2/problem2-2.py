import random


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = partition(arr, start, end)
    # 파티셔닝된 리스트에 재귀적으로 퀵정렬을 수행한다.
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)


def partition(arr, start, end):
    # get random pivot
    pivot = random.randrange(start, end)

    # 피벗의 값을 제일 왼쪽으로 옮긴다.
    arr[pivot], arr[start] = arr[start], arr[pivot]

    pivot = start

    i = start + 1
    # 왼쪽에서부터 파티셔닝을 실행한다.
    for j in range(start + 1, end + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # 피벗보다 작거나 같은 값 중 가장 오른쪽 인덱스에 있는 값과 피벗의 위치를 교환한다.
    arr[i - 1], arr[pivot] = arr[pivot], arr[i - 1]
    # 피벗의 인덱스를 반환한다.
    pivot = i - 1
    return pivot


def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if target < numbers[mid]:
            end = mid - 1
        if target > numbers[mid]:
            start = mid + 1
        if numbers[mid] == target:
            return arr[mid]

    if end < 0:
        return arr[start]

    return arr[end]


def solution(arr, S):
    max_val = -1

    i = 0
    a = arr[i]

    # a + b <= S를 만족시키는 b 중 가장 큰 값을 탐색한다.
    b = binary_search(arr, S - a)

    while a < b:
        target = S - arr[i]
        target = binary_search(arr, target)
        sum = arr[i] + target
        # a + b <= S를 만족하는 가장 큰 a + b를 갱신한다.
        max_val = max(max_val, sum)

        # 최댓값이 갱신됐을 때, a 와 b를 저장
        if sum == max_val:
            a = arr[i]
            b = target
        i += 1
    if a > b:
        a, b = b, a

    return a, b

n = input()
arr = list(map(int, input().rstrip().split(" ")))
S = int(input())


quick_sort(arr, 0, len(arr) - 1)
a, b = solution(arr, S)
print(a, b)
