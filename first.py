# Напишите функцию получающую на вход численные значения некоторой случайной величины и вероятности
# их появления, а возвращающую – ее математическое ожидание и дисперсию.


def first_task(x_list, p_list):
    x_list_length = len(x_list)
    m = 0
    d = 0

    for index in range(0, x_list_length):
        m += x_list[index] * p_list[index]
    for index in range(0, x_list_length):
        d += p_list[index] * ((x_list[index] - m) ** 2)
    return m, d


m = first_task([1, 2, 3, 4, 5, 6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(str(m[0]))
print(str(m[1]))
