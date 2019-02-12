# Напишите функцию реализующую скалярное произведение двух векторов произвольной длины.


def second_task(v1, v2):
    v_length = len(v1)
    result = 0

    for index in range(v_length):
        result += v1[index] * v2[index]

    return result


ab = second_task([3, -1], [-2, 7])
print(str(ab))
