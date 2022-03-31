#Please wrap all logic in functions:
"""
1. Заменить в произвольной строке согласные буквы на гласные.
"""
import random
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u", "y"]


def change_into_vowels(random_str):

    for letter in random_str:
        if letter.lower() in consonants:
            random_str = random_str.replace(letter, random.choice(vowels))
    return random_str


print(change_into_vowels("Gjjfnkiomsc kfgg nknkpo"))


#2. массив из словарей

data = [
  {'name': 'Viktor', 'city': 'Kyiv', 'age': 30 },
  {'name': 'Maksim', 'city': 'Dnipro', 'age': 20},
  {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
  {'name': 'Andrey', 'city': 'Kyiv', 'age': 34},
  {'name': 'Artem', 'city': 'Dnipro', 'age': 50},
  {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

"""
2.1. отсортировать массив из словарей по значению ключа ‘age'
"""


def sort_by_age(some_arg):
    sorted_data = sorted(some_arg, key=lambda x: x['age'])
    return sorted_data


print(sort_by_age(data))

"""
2.2. сгруппировать данные по значению ключа 'city'
"""


def group_by_city(some_arg):
    result_data = {}
    for item in some_arg:
        city = item.pop('city')
        if city in result_data:
            result_data[city].append(item)
        else:
            result_data[city] = [item]
    return result_data


print(group_by_city(data))


"""
3. У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
"""


def most_frequent(list_var) -> str:
    max_value = 0
    frequent_str = None
    for item in list_var:
        item_count = list_var.count(item)
        if item_count >= max_value:
            max_value = item_count
            frequent_str = item

    return frequent_str


print(most_frequent(['a', 'a', 'bi', 'bi', 'bi', 'di', 'di', 'di']))
