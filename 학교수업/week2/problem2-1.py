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
            return numbers[mid]

    # K가 배열 안에 없는 경우
    # K가 배열의 요소 중 가장 큰 값보다 더 크다면 탐색 과정에서 탐색 과정에서 start가 가리키는 인덱스가 배열의 범위를 벗어나게 되므로,
    # 이때 start의 바로 이전 인덱스를 가리키는 end의 값을 반환한다.
    if start >= len(numbers):
        return numbers[end]
    # K가 배열의 요소 중 가장 작은 수보다 작다면 탐색 과정에서 end가 가리키는 인덱스가 배열의 범위를 벗어나므로 가장 첫번째 값을 반환한다.
    if end < 0:
        return numbers[start]
    # 위의 두 경우가 아닐 경우, K의 값과 인접한 두 값을 K와 비교하여 더 가까운 값을 반환한다. 두 값이 같을 경우 더 작은 값을 반환한다.
    return numbers[start] if abs(numbers[start] - target) < abs(numbers[end] - target) else numbers[end]

n = int(input())
numbers = list(map(int, input().split(" ")))
target = int(input())

print(binary_search(numbers, target))
