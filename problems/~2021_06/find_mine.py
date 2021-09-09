col, row = map(int, input().split(" "))

matrix = []
for i in range(col):
    matrix.append([char for char in input()])

dx = [-1, 0, 1]
dy = [-1, 0, 1]

for i in range(col):
    for j in range(row):
        if matrix[i][j] == '.':
            count = 0
            for x in dx:
                for y in dy:
                    if (i == 0 and x == -1) or (i == col-1 and x == 1) or (j == 0 and y == -1) or (j == row-1 and y == 1):
                        continue
                    if matrix[i + x][j + y] == '*':
                        count += 1
            matrix[i][j] = str(count)

for col in matrix:
    print("".join(col))