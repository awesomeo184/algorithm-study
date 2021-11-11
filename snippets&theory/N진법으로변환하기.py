def conversion(number, n):
    result = []
    current = number

    if number == 0:
        result.append(0)

    while current > 0:

        if current % n < 10:
            result.append(current % n)
        else:
            result.append(chr(current % n - 10 + ord("A")))

        current //= n

    result = reversed(result)
    return "".join(map(str, result))