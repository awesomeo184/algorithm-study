from typing import List

'''
algorithm queens(k): # x[k]를 결정
    if k >= n:
        return
    for c in range(n):
        if place(k, c):
            x[k] = c
            queens(k+1)
    
'''


def canPlace(x, k, c):
    for j in range(k):
        if x[j] == c or abs(x[j] - c) == abs(j - k):
            return False
    return True

def queens(x: List[int], k: int, n: int):
    if k >= n:
        print(x)
        return
    for c in range(n):
        if canPlace(x, k, c):
            x[k] = c
            queens(x, k+1, n)

queens(x=[0,0,0,0], k=0, n=4)