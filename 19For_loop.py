'''for loop is used when we now the number of iteration
for condition:
    <block of code'''

#print 1 to 10 using for loop
for i in range(1,11): #range(start,end-1,step)
    print(i,end=' ') 
print('\n')
#by using step can print odd numbers
for i in range(1,50,2):
    print(i,end=' ')
    
#print square number from 1 to 10
for i in range(1,11):
    print(f'square of {i}={i*i}')

string=input('enter a string: ')
for ch in string:
    print(ch,end=',')
    
#enumerate function
name='sindhu dodmane'
for index,letter in enumerate(name):
     print(f'the letter "{letter}" is in index {index}\n')
     
#nested for loop for multiplication table
for i in range(1,11):
    for j in range(1,11):
        print(f'{i}x{j}= {i*j}')
        j+=1
    i+=1 
    
#take dictionary as example for enumerate()
my_dict={'jan':1,'feb':2,'march':3}
for key,value in enumerate(my_dict):
    print(key,value) 

#print even numbers between 1 to 50
for i in range(1,50):
    if i%2==0:
        print(i,end=' ') 
        
#find sum of numbers from 1 to N
n=int(input('enter value of  n:'))
sum=0
for i in range(1,n+1):
    sum+=i
print(f'sum of numbers between 1 to {n} is: {sum}')

#count the vowels in string
string_1=input('enter a string: ')
count=0
for ch in string_1:
    if ch in "aeiou":
        count+=1
print(f'total number of vowels in given string: {count}')

#print factorial of given number using for loop
num=int(input('enter a number: '))
fact=1
for i in range(1,num):
    fact*=num
    num-=1
print(f'factorial of given number is : {fact}')

#find largest element in list
my_list=[4,6,8,2,9,3,10]
largest=0
for i in my_list:
    if i>largest:
        largest=i
print(largest) #10


