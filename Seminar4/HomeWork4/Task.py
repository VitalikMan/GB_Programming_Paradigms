import math

def calculate_pearson_correlation(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Длины массивов должны быть одинаковыми")

    sum_x = sum(x)  # Вычисляем сумму элементов массива x
    sum_y = sum(y)  # Вычисляем сумму элементов массива y
    mean_x = sum_x / n  # Вычисляем среднее значение для массива x
    mean_y = sum_y / n  # Вычисляем среднее значение для массива y

    numerator = 0  # Инициализируем переменную для числителя
    sum_x_squared = 0  # Инициализируем переменную для суммы квадратов отклонений x
    sum_y_squared = 0  # Инициализируем переменную для суммы квадратов отклонений y

    for i in range(n):
        diff_x = x[i] - mean_x  # Вычисляем отклонение x[i] от среднего значения
        diff_y = y[i] - mean_y  # Вычисляем отклонение y[i] от среднего значения
        numerator += diff_x * diff_y  # Обновляем значение числителя
        sum_x_squared += diff_x ** 2  # Обновляем значение суммы квадратов отклонений x
        sum_y_squared += diff_y ** 2  # Обновляем значение суммы квадратов отклонений y

    denominator = math.sqrt(sum_x_squared * sum_y_squared)  # Вычисляем знаменатель
    correlation = numerator / denominator  # Вычисляем коэффициент корреляции Пирсона

    return correlation

x = [10, 20, 30, 40, 50]
y = [5, 10, 15, 20, 25]

correlation = calculate_pearson_correlation(x, y)
print(f"Коэффициент корреляции Пирсона: {correlation}")
