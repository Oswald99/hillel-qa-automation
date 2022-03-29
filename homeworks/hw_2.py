list_numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

"""
1.1.Убрать из него повторяющиеся элементы
"""
list_without_doubles = list(set(list_numbers))
print(list_without_doubles)

"""
1.2.Вывести 3 наибольших числа из исходного массива
"""
sorted_list = sorted(list(set(list_numbers)), reverse=True)
print(sorted_list[:3])

""""
1.3) Вывести индекс минимального элемента массива
"""

print(list_numbers.index(min(list_numbers)))

""""
1.4) вывести исходный массив в обратном порядке
"""
print(list_numbers[::-1])

"""
2. Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
"""

list_result = list(range(0, 101, 2))
print(list_result)

"""
3. Найти общие ключи в двух словарях:
"""

dict_one = {"a": 1, "b": 2, "c": 3,  "d": 4}
dict_two = {"a": 6, "b": 7, "z": 20, "x": 40}
same_keys = set(dict_one.keys()).intersection(dict_two.keys())
print(same_keys)

"""
4. Сгенерировать dict() из списка ключей ниже по формуле (key : key* key)
"""

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict_from_keys = {key: key*key for key in keys}
print(dict_from_keys)
