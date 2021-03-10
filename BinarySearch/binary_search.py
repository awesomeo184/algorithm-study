def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search_with_loop(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] > target:
            end = mid - 1
        if arr[mid] < target:
            start = mid + 1
        if arr[mid] == target:
            return mid

    return -1


def binary_search_with_recursion(arr, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if arr[mid] > target:
        return binary_search_with_recursion(arr, target, start, mid - 1)
    if arr[mid] < target:
        return binary_search_with_recursion(arr, target, mid + 1, end)
    if arr[mid] == target:
        return mid


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
arr.sort()
target = 18

result = sequential_search(arr, target)
result1 = binary_search_with_loop(arr, target)
result2 = binary_search_with_recursion(arr, target, 0, len(arr))

print(result)
print(result1)
print(result2)