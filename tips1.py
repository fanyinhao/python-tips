# ---------------------------------start-------------------------------
# ZeroDivisionError: division by zero
def division_by_zero():
    param_a = 0
    print(param_a > 0 and param_a / 0 > 1)


# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 函数是Python中的一等公民
# 它们可以作为参数传递给其他函数，作为其他函数的值返回，并且分配给变量并存储在数据结构中。

def my_func(a, b):
    return a + b


funcs = [my_func]
print(funcs[0])  # <function my_func at 0x107012230>
print(funcs[0](2, 3))  # 5
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# is 和 == 的区别, is表示两个变量指向同一个对象, == 表示两个变量值相等
a = [1, 2, 3]
b = a
print(a is b)  # Ture
print(a == b)  # Ture
c = list(a)
print(a is c)  # False
print(a == c)  # Ture
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 假设我们要交换a和b的值...
a, b = b, a
# ---------------------------------end-------------------------------

# timeit模块可以评估少量Python代码的执行时间
import timeit

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))  # 0.3412662749997253
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))  # 0.2996307989997149
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))  # 0.24581470699922647


# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 函数参数解包
def my_func_to_unpack(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}
my_func_to_unpack(*tuple_vec)  # 1, 0, 1
my_func_to_unpack(**dict_vec)  # 1, 0, 1
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 字典的标准字符串repr很难阅读
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)  # {'b': 42, 'c': 12648430. 'a': 23}

# The "json" module can do a much better job:
import json

print(json.dumps(my_mapping, indent=4, sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# Namedtuples
# 使用namedtuple比手动定义类短
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 3812.4)
print(my_car.color)  # 'red'
print(my_car.mileage)  # 3812.4

# We get a nice string repr for free:
print(my_car)  # Car(color='red', mileage=3812.4)
# 与元组一样，namedtuple是不可变的
# my_car.color = 'blue'  # AttributeError: "can't set attribute"
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 调用get()时，它将检查字典中是否存在给定键。如果确实存在，则返回该键的值;如果不存在，则返回默认参数的值。
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))  # "Hi Alice!"
print(greeting(333333))  # "Hi there!"
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 如何按值对Python字典排序（==获取按值排序的表示形式）
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
import operator

print(sorted(xs.items(), key=operator.itemgetter(1)))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------

# 从多个对象中找出一个对象的办法
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# 真值校验
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
# ---------------------------------end-------------------------------

# ---------------------------------start-------------------------------
# 合并dict
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)  # {'c': 4, 'a': 1, 'b': 3}

# python 2.x 可以这么处理
z = dict(x, **y)
print(z)  # {'a': 1, 'c': 4, 'b': 3}
# ---------------------------------end-------------------------------
