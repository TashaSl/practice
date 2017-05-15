'''
Поле для игры сапёр представляет собой сетку размером n×m. В ячейке сетки может находиться или отсутствовать мина. 

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается
число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится описание поля
в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"),
при этом число означает количество мин в соседних ячейках поля.
'''

from functools import reduce

n, m = map(lambda x: int(x), input().split())

arr = reduce(lambda A, x: A + [list(input())], range(n), [])

def get_possible_values(u, border):
    return list(filter(lambda x: 0 <= x < border, range(u - 1, u + 2)))

def get_combination(arr1, arr2):
    return reduce(lambda A, el: A + list(zip([el] * len(arr2), arr2)), arr1, [])

def get_nearest_cell_cord(coord):
    return get_combination(get_possible_values(coord[0], n), get_possible_values(coord[1], m)) 

def is_bomb(coord):
    return True if arr[coord[0]][coord[1]] == '*' else False

def get_num_bomb_cell(coord):
    return reduce(lambda A, coord: A + 1 if is_bomb(coord) else A, get_nearest_cell_cord(coord), 0)

def get_num_bomb_matrix():
    return list(map(lambda el: str(get_num_bomb_cell(el)) if not is_bomb(el) else '*', get_combination(range(n), range(m))))

def result(matrix):
    return reduce(lambda A, u: A + ''.join(matrix[u * m : (u + 1) * m]) + '\n', range(n), '')

print(result(get_num_bomb_matrix()))
