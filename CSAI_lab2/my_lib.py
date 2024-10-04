def fibonacci(n: int):
    """
    Определяет первые n чисел Фибоначчи.
    :param n: Количество чисел Фибоначчи
    :return: Список первых n чисел Фибоначчи
    """
    if n <= 0:
        raise ValueError("n должно быть больше 0")

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]


def bubble_sort(arr: list):
    """
    Сортирует список чисел методом пузырька.
    :param arr: Список чисел
    :return: Отсортированная копия списка
    """
    n = len(arr)
    sorted_arr = arr[:]

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


def calculator(a: float, b: float, operator: str):
    """
    Выполняет арифметическое действие над двумя числами.
    :param a: Первое число
    :param b: Второе число
    :param operator: Оператор (+, -, *, /)
    :return: Результат арифметической операции
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    else:
        raise ValueError("Некорректный оператор")
