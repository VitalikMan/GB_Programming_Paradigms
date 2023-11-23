# Задача №2
# Написать, точно такую же процедуру, как в первой задаче, но в декларативном стиле.

# Здесь мы используем встроенную функцию sorted(), которая сортирует список чисел в порядке возрастания.
# Параметр reverse=True указывает на то, что мы хотим отсортировать в порядке убывания.

def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

numbers = [10, 1, 4, 6, 8]
print("Не сортированный список: ", numbers)

sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания: ", sorted_numbers)  # [10, 8, 6, 4, 1]
