# Задание:
# Написать программу на языке Prolog для вычисления суммы элементов списка.
# На вход подаётся целочисленный массив.
# На выходе - сумма элементов массива.

# # Базовый случай - сумма пустого списка равна 0.
# sum_list([], 0).
#
# # Вычисляем сумму элементов списка
# sum_list([X|Xs], Sum) :-
#     sum_list(Xs, RestSum),
#     Sum is X + RestSum.
#
# # Выполнение запроса
# ?- sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Result.
