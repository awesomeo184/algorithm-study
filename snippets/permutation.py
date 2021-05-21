from typing import List


# nPr
# 크기가 n인 배열 arr에서 r개를 뽑아 나열
def permutation(arr: List[int], r: int, temp: List[int], current: int, visited: List[bool]):
    if current == r:
        print(temp)
    else:
        for i in range(len(arr)):
            if not visited[current]:
                visited[i] = True
                temp[current] = arr[i]
                permutation(arr, r, temp, current + 1, visited)
                visited[i] = False


# n∏r
# 크기가 n인 배열 arr에서 중복을 허용하여 r개를 뽑아 나열
def permutation_with_repetition(arr: List, r: int, temp: List, current: int):
    if current == r:
        print(temp)
    else:
        for i in range(len(arr)):
            temp[current] = arr[i]
            permutation_with_repetition(arr, r, temp, current + 1)


print("------permutaion-------")
permutation(arr=[1, 2, 3], r=2, temp=[0, 0], current=0, visited=[False, False, False])

print()

print("------permutaion with repetition-------")
permutation_with_repetition(arr=[1, 2, 3], r=2, temp=[0, 0], current=0)
