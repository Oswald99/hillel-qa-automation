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


#some_value('My string')
# some_value(46)


"""
Написать декоратор, который будет кешировать значения аргументов и результаты работы вашей функции и записывать
его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
«Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
количество раз обращений в cache.
"""


def decorator_cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            wrapper.cache_call += 1
            print(f'Used cache with counter = {wrapper.cache_call}')
            return cache[args]
        else:
            wrapper.fun_call += 1
            cache[args] = func(*args)
            print(f'Function executed with counter = {wrapper.fun_call}, function result = {cache[args]}')
            return cache[args]

    wrapper.cache_call = 0
    wrapper.fun_call = 0
    return wrapper


@decorator_cached
def multiply_numbers(x, y):
    result = x * y
    return result


multiply_numbers(1, 2)
multiply_numbers(1, 5)
multiply_numbers(2, 4)
multiply_numbers(3, 2)
multiply_numbers(3, 2)
multiply_numbers(10, 11)
multiply_numbers(1, 2)
