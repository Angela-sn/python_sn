'''
 1.Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os

string = "C:\АНЖЕЛА\Desktop\Seminar_5.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f' строка: {string} \n кортеж: путь, имя файла, расширение файла: {fun(string)}')