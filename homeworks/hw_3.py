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



'''
#Дан массив из словарей

data = [
  {'name': 'Viktor', 'city': 'Kyiv', 'age': 30 },
  {'name': 'Maksim', 'city': 'Dnipro', 'age': 20},
  {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
  {'name': 'Andrey', 'city': 'Kyiv', 'age': 34},
  {'name': 'Artem', 'city': 'Dnipro', 'age': 50},
  {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

2.1) отсортировать массив из словарей по значению ключа ‘age'

2.2) сгруппировать данные по значению ключа 'city'



3) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.

Например:



def most_frequent(list_var):

  #your code is here

  return



most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
'''
