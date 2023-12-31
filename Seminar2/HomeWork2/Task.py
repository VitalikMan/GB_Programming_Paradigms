# Домашнее задание 2:
# Таблица умножения.
# Условие:
# На вход подается число n.
# Задача:
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
#
# Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9


# Для решения этой задачи я бы предложил использовать парадигму императивного программирования.
# Императивное программирование подразумевает последовательное выполнение команд.

n = int(input("Введите число n: "))
print("-" * 10)
for i in range(1, n+1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print("-" * 10)


# Пояснение:
#
# Пользователю предлагается ввести число n с помощью функции input().
# С помощью функции range(1, n+1) мы создаем последовательность чисел от 1 до n, включая n.
# Вложенный цикл for j in range(1, 10) создает последовательность чисел от 1 до 9.
# Внутри вложенного цикла выводится результат умножения текущих значений переменных i и j с помощью функции print().
# Таким образом, скрипт последовательно выводит таблицу умножения всех чисел от 1 до введенного числа n.