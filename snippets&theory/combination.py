from typing import List

# nCr
# 크기가 n인 배열 arr에서 r개를 뽑는 경우의 수
def combination(arr: List[int], r: int, temp: List[int], current: int, start: int):
    if current == r:
        print(temp)
    else:
        for i in range(start, len(arr)):
            temp[current] = arr[i]
            combination(arr, r, temp, current + 1, i + 1)

# nHr
# 크기가 n인 배열 arr에서 중복을 허용하여 r개를 뽑는 경우의 수
def combination_with_repetition(arr: List[int], r: int, temp: List[int], current: int, start: int):
    if current == r:
        print(temp)
    else:
        for i in range(start, len(arr)):
            temp[current] = arr[i]
            combination_with_repetition(arr, r, temp, current+1, i)

print("----combination----")
combination(arr=[1, 2, 3, 4], r=2, temp=[0, 0], current=0, start=0)

print()

print("----combination with repetition----")
combination_with_repetition(arr=[1, 2, 3, 4], r=2, temp=[0, 0], current=0, start=0)
