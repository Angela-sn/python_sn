# 2.2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction
import math

str_1 = input("Введите первую дробь: ")
str_2 = input("Введите вторую дробь: ")

def shortenFraction(n: int, m: int):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return str(n // k) + "/" + str(m // k)
        else:
            k -= 1
    return str(n) + "/" + str(m)

def sum_fractions(str_1, str_2):
    num_1 = str_1.split("/")
    num_2 = str_2.split("/")
    lcm_fraction = math.lcm(int(num_1[1]), int(num_2[1]))   # НОЗ дроби
    numeratorFraction_1 = int(lcm_fraction / int(num_1[1]) * int(num_1[0]))
    numeratorFraction_2 = int(lcm_fraction / int(num_2[1]) * int(num_2[0]))
    return shortenFraction(numeratorFraction_1 + numeratorFraction_2, lcm_fraction)

def mult_fraction(str1, str2):
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    #return int(num_1[0]) * int(num_2[0]) / (int(num_1[1]) * int(num_2[1]))
    return shortenFraction(int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1]))

def check_fraction(str1, str2, operation):
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    if operation == "*":
        return Fraction(int(num_1[0]), int(num_1[1])) * Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "+":
        return Fraction(int(num_1[0]), int(num_1[1])) + Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "-":
        return Fraction(int(num_1[0]), int(num_1[1])) - Fraction(int(num_2[0]), int(num_2[1]))
    else:
        return Fraction(int(num_1[0]), int(num_1[1])) / Fraction(int(num_2[0]), int(num_2[1]))

print("Расчет по программе:")
print(f'{str_1} * {str_2} = {mult_fraction(str_1, str_2)}')
print(f'{str_1} + {str_2} = {sum_fractions(str_1, str_2)}')

print("\nПроверка по Fraction:")

print(f"{str_1} * {str_2} = {Fraction(int(str_1.split('/')[0]), int(str_1.split('/')[1])) * Fraction(int(str_2.split('/')[0]), int(str_2.split('/')[1]))}")
print(f"{str_1} + {str_2} = {Fraction(int(str_1.split('/')[0]), int(str_1.split('/')[1])) + Fraction(int(str_2.split('/')[0]), int(str_2.split('/')[1]))}")
