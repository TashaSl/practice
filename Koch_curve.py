'''
Кривая Коха -- это простой геометрический фрактал. 
Строится этот фрактал следующим образом: берётся отрезок, разделяется на
три равных части. Вместо средней части вставляется два таких же отрезка,
поставленные под углом 60 градусов друг к другу.
Этот процесс повторяется на каждой итерации: каждый отрезок заменяется
четырьмя.
Напишите программу, которая принимает на вход число n − количество итераций
генерации кривой и выводит последовательность углов поворота при рисовании
соответствующей линии от начальной точки к конечной, без отрыва пера.
Формат ввода:
Строка с целым числом nn, 1≤n≤10.
Формат вывода:
Строки, содержащие последовательность поворотов. Каждый поворот указывается
на отдельной строке как слово "turn" и угол поворота в градусах. Угол поворота
должен находиться в интервале [-180; 180].
'''
from functools import reduce

make_string = lambda x: x + 'turn 60\n' + x + 'turn -120\n' + x + 'turn 60\n' + x

result = lambda n: reduce(lambda A, x: make_string(A), range(n), '')

print(result(int(input()))[:-2])
