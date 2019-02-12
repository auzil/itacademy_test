# Игральную кость бросили N раз. Какова вероятность того, что M раз выпадет число
# не менее S. Напишите алгоритм решения данной задачи, для любых N, M и S.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def calculate_combination_number(N, m):
    return factorial(N) / (factorial(m) * factorial(N-m))


def task_four(N, S, m):
    p = S/6
    q = 1 - p

    return calculate_combination_number(N, m) * (p ** m) * (q ** (N - m))


print(task_four(1, 3, 1))
