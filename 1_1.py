'''
Задача взята с курса "Адаптивный тренажер Python" на stepic.org
Последовательность n>0n>0 целых чисел называется jolly jumper в случае, 
если значения абсолютных разностей последовательных элементов принимают
все возможные значения между 11 и n−1n−1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper
последовательностью, так как абсолютные разности равны 4 1 3 2,
соответственно, а n−1=4n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая
последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1≤n≤100001≤n≤10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.
'''

# ввод массива
arr = list(map(lambda x: int(x), input().split()))

# рассчет значений абсолютных разностей последовательных элементов
func_razn = lambda arr: map(lambda x: abs(x[0] - x[1]), zip(arr, arr[1:]))

# выводим результат
result = print('Jolly') if sorted(list(func_razn(arr))) == list(range(1, len(arr))) or len(arr) == 1 else print('Not jolly')
