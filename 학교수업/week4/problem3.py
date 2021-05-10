n = int(input())
u = list(map(int, input().split(" ")))
l = list(map(int, input().split(" ")))
u_to_l = list(map(int, input().split(" ")))
l_to_u = list(map(int, input().split(" ")))

tmp_u = 0
tmp_l = 0

for i in range(n):
    tmp_u += u[i]
    tmp_l += l[i]
    tmp_u = min(tmp_u, tmp_l + l_to_u[i])
    tmp_l = min(tmp_l, tmp_u + u_to_l[i])

print(min(tmp_u + u[-1], tmp_l + l[-1]))