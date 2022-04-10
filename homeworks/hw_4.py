import functools
"""
Написать свой декоратор, который будет проверять остаток от деления числа 100 на результат работы функции.
Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления
"""


def check_remainder_of_division(func):
    def wrapper(*args):
        result = 100 % func(*args)
        if result == 0:
            print('We are OK!')
        else:
            print(f'Bad news guys, we got {result}')

    return wrapper


@check_remainder_of_division
def func_division(numb):
    return numb


func_division(101)
func_division(100)


"""
Написать декоратор, который будет выполнять предпроверку типа аргумента, который передается в вашу функцию.
Если это int, тогда выполнить функцию и вывести результат, если это str(),
тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))
"""


def decorator_check_value_type(func):
    def wrapper(*args):
        try:
            print(int(func(*args)))
        except ValueError:
            raise ValueError("String type is not supported")
    return wrapper


@decorator_check_value_type
def some_value(b):
    return b


some_value('My string')
# some_value(46)
