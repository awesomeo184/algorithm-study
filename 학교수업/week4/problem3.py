n = int(input())
u = list(map(int, input().split()))
l = list(map(int, input().split()))
u_to_l = list(map(int, input().split()))
l_to_u = list(map(int, input().split()))

tmp_u = 0
tmp_l = 0

for i in range(n):
    # 각 도로에서 다음 노드로 이동할때 비용을 추가한다.
    tmp_u += u[i]
    tmp_l += l[i]

    # 도로를 변경할 때 비용
    up_cost = l_to_u[i]
    down_cost = u_to_l[i]

    # 다음 노드로 이동할 때의 비용과 도로를 변경할 때의 비용 중 작은 값을 선택한다.
    tmp_u = min(tmp_u, tmp_l + up_cost)
    tmp_l = min(tmp_l, tmp_u + down_cost)

# 마지막 노드에서 목적지로 이동하는데 드는 비용을 추가한다.
print(min(tmp_u + u[-1], tmp_l + l[-1]))