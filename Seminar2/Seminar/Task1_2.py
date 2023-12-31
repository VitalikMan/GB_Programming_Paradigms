# Структурное программирование

# Основная логика программы
def main():
    num1 = 10
    num2 = 5

    # Вычисление суммы
    result = num1 + num2
    print("Сумма:", result)

    # Вычисление разности
    result = num1 - num2
    print("Разность:", result)

    # Вычисление произведения
    result = num1 * num2
    print("Произведение:", result)

    # Вычисление частного
    if num2 != 0:
        result = num1 / num2
        print("Частное:", result)
    else:
        print("Деление на ноль недопустимо")

if __name__ == "__main__":
    main()

# ==============================================

# Процедурное программирование

# Функция для сложения двух чисел
def add(x, y):
    return x + y

# Функция для вычитания двух чисел
def subtract(x, y):
    return x - y

# Функция для умножения двух чисел
def multiply(x, y):
    return x * y

# Функция для деления двух чисел
def divide(x, y):
    if y == 0:
        return "Деление на ноль недопустимо"
    return x / y

# Основная логика программы
def main():
    num1 = 10
    num2 = 5


if __name__ == "__main__":
    main()
