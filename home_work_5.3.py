'''
3.Создайте функцию генератор чисел Фибоначчи
'''
a = int(input('введите число:  '))
def fibonacсi(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacсi(a)))
