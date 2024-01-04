# Урок 2. Простые типы данных

#1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

DIV_HEX = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

original_num = int(input("Введите целое число: "))
num = original_num
result: str = ""
while num > 0:
    result = str(hex_data[num % DIV_HEX]) + result
    num //= DIV_HEX
print(f'Число {original_num} в {DIV_HEX} системе 0x{result}')

hex_string = hex(original_num)  # проверка
print(f'Проверка: число {original_num} в 16-ой системе счисления = {hex(original_num)}')
