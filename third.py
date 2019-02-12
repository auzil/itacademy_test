# Напишите функцию реализующую нахождение длины вектора произвольной размерности.


def third_task(v):
    result = 0

    for element in v:
        result += element

    return result ** 0.5


a = third_task([3, -1])
print(str(a))
