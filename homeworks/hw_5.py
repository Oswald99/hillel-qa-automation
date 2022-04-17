""""
Реализовать класс, который бы производил разные операции над 2мя переданными числами.
proccess_input = ProcessInput(a=20, b=10)
Пример Использования:
print(proccess_input.add()). # выведет 30
print(proccess_input.subtract()). # выведет 10
print(proccess_input.multiple()). # выведет 200
print(proccess_input.divide()). # выведет 2
"""


class Calculation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            raise ZeroDivisionError("ZeroDivisionError occurs when num1 is divided by zero")


proccess_input = Calculation(num1=20, num2=6)
print(proccess_input.add())
print(proccess_input.subtract())
print(proccess_input.multiple())
print(proccess_input.divide())