#problem with input()method
# input() function always retuen string even if user enter numbers it is difficult to store numberlist.

n=int(input('enter number of elements: '))
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)
print(numbers)

#spl concept is list comprehension 
# it provide a 'shorter syntax' while creating a new from existing list.
names=['Janu','banu','James','Michael','Jimmy']
J_names=[]
for name in names:
    if 'J' in name:
        J_names.append(name)
print(J_names)

#syntax for list comprehension : list=[expression for item in iterable if condition==True]

name_copy=[name for name in names]
print(name_copy)

#instead of 1st code we can use list comprehension

J_names=[name for name in names if 'J' in name]
print(J_names)