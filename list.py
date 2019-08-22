#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(r"**************************************************************")
print("list是一个可变的有序表，注意是方括号")
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print("classmates[0]:",classmates[0])
print("classmates[1]:",classmates[1])
print("classmates[2]:",classmates[2])
#print("越界错误：",classmates[3])

print('- - - - - - - - - - - - - - - - - - - ')
print("取最后一个元素:",classmates[-1])
print("取倒数第二个元素:",classmates[-2])
print("classmates[-3]:",classmates[-3])
#print("越界错误：",classmates[-4])

print('- - - - - - - - - - - - - - - - - - - ')
print("list是一个可变的有序表,可添加/删除元素")
classmates.append('Adam')
print("classmates.append('Adam'):",classmates)
classmates.insert(1, 'Jack')
print("classmates.insert(1, 'Jack'):",classmates)
print("删除末尾的元素：classmates.pop():",classmates.pop())
print(classmates)
print("删除指定的元素：classmates.pop(1):",classmates.pop(1))
print(classmates)
print("替换元素：classmates[1]='Sarah':")
classmates[1]='Sarah'
print(classmates)

print('- - - - - - - - - - - - - - - - - - - ')
print("list里面的元素的数据类型也可以不同:")
L=['Apple', 123, True]
print(L)
print("len(L):",len(L))
print("list元素也可以是另一个list:")
L2=['python', 'java', L, 'scheme']
print(L2)
print("len(L2):",len(L2))
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print("len(s):",len(s))

print('- - - - - - - - - - - - - - - - - - - ')
print(r'''tuple,元组,是一种有序列表,和list非常类似,但是一旦初始化就不能修改,注意是圆括号.
一个tuple,在定义的时候,tuple的元素就必须被确定下来,没有append(),insert()这样的方法''')
t = (1, 2)
print(t)
print("定义一个空的tuple:")
t=()
print(t) 
print(r"只有1个元素的tuple定义时必须加一个逗号")
t=(1,)
print(t)
print("以下定义的不是tuple，是1这个数")
t=(1)
print(t)

print('- - - - - - - - - - - - - - - - - - - ')
print("以下tuple定义的时候有3个元素，分别是'a'，'b'和一个list")
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

print('- - - - - - - - - - - - - - - - - - - ')
print("循环")
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print('- - - - - - - - - - - - - - - - - - - ')
print(list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print('- - - - - - - - - - - - - - - - - - - ')
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

print('- - - - - - - - - - - - - - - - - - - ')
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,','%s!' % x)
 
print('- - - - - - - - - - - - - - - - - - - ')
i = 0
while i <= 100:
    if i >= 8: # 当n = 8时，条件满足，执行break语句
        break  # break语句会结束当前循环
    i = i + 1
    print(i)
print("END")   

print('- - - - - - - - - - - - - - - - - - - ')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)