
#swapping of two numbers using temp and without temp
print('swapping of two numbers')
a=10
b=20
print('before swapping:',a,b)
temp=a
a=b
b=temp
print('after swapping:a',a,b)

#without temp
a,b = b,a #using variable assignment
print('after swapping:',a,b)

#sum and average of 3 numbers
x=int(input('enter first number: '))
y=int(input('enter second number: '))
z=int(input('enter third number: '))
sum=x+y+z
avg=sum/3
print('Sum:  ',sum)
print('Average: ', avg)

#Area and perimeter of rectangle
length=int(input('enter length of trctangle:'))
width=int(input('enter width of trctangle:'))
print('area= ',length*width)
print('perimeter: ',2*(length+width))

#check whether given number is odd or even
num=int(input('enter a number: '))
if num%2==0:
 print('even')
else:
   print('odd')

#sqaure and cube
sqr= num**2
cube= num**3
print(f'square: {sqr} and cube:{cube}')

#celsius to fahrenheit
c=float(input('enter temperature in celsius:'))
f=c*9/5+32
print('temperature in fahrenheit is:',f)

#simple interest
p=int(input('enter value of p:'))
t=int(input('enter value of t:'))
r=int(input('enter value of r:'))
s=(p*t*r)/100
print('simple interest:',s)

