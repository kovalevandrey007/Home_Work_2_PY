# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем. Программа
# должна возвращать сумму и произведение* дробей. Для
# проверки своего кода используйте модуль fractions.
import fractions


def fraction(a, b):
    sum1 = a + b
    comp = a * b
    print(f'Сумма дробей = {sum1}\nПроизведение дробей = {comp}')

a = fractions.Fraction(1, 5)
b = fractions.Fraction(2, 3)
fraction(a, b)
