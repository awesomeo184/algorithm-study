def maximum(array, left, right):
    if left == right:
        return array[left]
    if left < right:
        mid = (left + right) // 2
        left_max = maximum(array, left, mid)
        right_max = maximum(array, mid + 1, right)

        if (left_max > right_max):
            return left_max
        else:
            return right_max

array = [1, 4, 6, 3, 4, 2, 8, 10]

print(max(array))
print(maximum(array, 0, len(array)-1))