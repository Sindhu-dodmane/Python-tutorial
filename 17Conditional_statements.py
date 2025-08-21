'''Conditional statements
  1. if statement
  2. if else statement
   3.nested if statement(elif)'''
#if statement
x=10
if x==10:
    print('x is 10')

#check number is even or odd using if-else statement
number= int(input('enter a number: '))
if number%2==0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')  # result = "even" if num %2==0 else "odd"

#check if the year is leap year or not
year=int(input('enter the year: '))
if (year % 4 ==0 )or (year % 400==0 )and (year % 100 !=0):
    print('{} is leap year'.format(year))
else:
    print('{} is not leap year'.format(year)) 

#find the leargest of 3 numbers
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))
if a>b and a>c:
    print(f'{a} is larger number than {b,c}')
elif b>a and b>c:
    print(f'{b} is larger number than {a,c}')
else:
    print(f'{c} is larger number than {a,b}') 

#check whether a character is vowel or consonant
char=input('enter the character: ')
if char.lower() in 'aeiou':
    print(f'{char} is vowel ')
else:
    print(f'{char} is consonant ') 

#find second largest number among the numbers
num=int(input('enter a number of element: '))
numbers=[]
for i in range(num):
     x=input('enter number:')
     numbers.append(x)
numbers.sort()
print('second largest number is',numbers[-2])

#check whether the number is prime
num1=int(input('enter the number: '))
if num1>1:
    is_prime=True
    for i in range(2,num1):
        if num1 % i ==0:
            is_prime=False
            break
    if is_prime:
           print(f'{num1} is prime ')
    else:
            print(f'{num1} is  not prime ')
else:
    print(f'{num1} is  not prime ') 

#check if a character is an alphabet,digit or special character
character=input('enter the character: ')
if character.isalpha():
    print(f'{character} is an alphabet')
elif character.isdigit():
    print(f'{character} is digit')
else:
    print(f'{character} is special character')

#check the triangle is valid or not
a=int(input('enter the first side of triangle: '))
b=int(input('enter the second side of triangle: '))
c=int(input('enter the third side of triangle: '))
if (a+b>c) and (b+c>a) and (a+c>b):
    print('valid triangle')
else:
    print('invalid triangle')

#checkif number is Armstrong
num = int(input("Enter number: "))
temp = num
sum_of_cubes = 0

while temp > 0:
    digit = temp % 10

    sum_of_cubes += digit ** 3
    temp //= 10

if sum_of_cubes == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#Find quadrant of a point(x,y)
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
else:
    print("Point lies on axis")

#find second largest among 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Second largest:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second largest:", b)
else:
    print("Second largest:", c)


 