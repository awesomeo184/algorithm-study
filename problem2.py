def get_max_index_and_value(array):
    # 가장 높은 주식 가격과 그 인덱스를 반환한다.
    max_price = max(array)
    max_index = array.index(max_price)

    return max_index, max_price


def split_by_index(array, index):
    # 가장 높은 가격을 기준으로 리스트를 좌, 우로 분리한다.

    # 가장 높은 가격이 첫 날이나 마지막 날일 경우, 각각 좌, 우로 빈 리스트를 반환한다.
    if index == 0:
        return [], array[1:]
    elif index == len(array) - 1:
        return array[:-1], []

    left = array[:index]
    right = array[index + 1:]

    return left, right


def get_profit(array):
    total = 0

    # 더 이상 분리할 리스트가 없는 경우 0을 반환하여 재귀를 종료한다.
    if not array:
        return 0

    # 최대 가격과 그 인덱스를 반환한다.
    max_index, max_price = get_max_index_and_value(array)

    # 최대 가격을 기준으로 리스트를 좌우로 분리한다.
    left, right = split_by_index(array, max_index)

    # 가장 높은 가격에 도달하기 전 날의 주식은 모두 구매한 후 최대 가격에 판다.
    total += len(left) * max_price - sum(left)

    # 가장 높은 가격에 도달 한 이후에는 다시 그날 이후부터 최대 가격을 찾아 앞의 과정을 반복한다.
    total += get_profit(right)

    return total


n = int(input())
prices = list(map(int, input().split()))

print(get_profit(prices))
