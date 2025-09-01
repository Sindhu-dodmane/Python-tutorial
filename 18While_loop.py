'''while loop and nested while loop
while condition:
      <block of code> '''
#print the numbers 1 to 10 using while loop
'''x=1
while x<=10:
    print(x ,end=' ')
    x+=1 
print("\n") '''
    
#print even numbers between 1 to 50
'''x=1
while x<50:
      if x%2==0:
            print(x,end=',')
      x = x+1
print('\n')'''

#print multiplication table eg,5
'''x=1
while x<=10:
      print(f'5x{x}= {5*x}')
      x+=1
print('\n') '''

#find factorial of a number
'''num=int(input('enter a number: '))
fact=1
while num>=1:
    fact=fact*num
    num=num-1
print(fact)'''
      
      
#sum of digits
'''number=int(input('enter a number: '))
s=0
while number>0:
      digit=number%10
      s+=digit
      number//=10
print('sum of digits: ',s)'''

#reverse a given number
'''num=int(input('enter a number: '))
rev=0
while num>0:
      digit=num%10
      rev=rev*10+digit
      num//=10
print('reversed number:',rev)'''

#same logic for palindrome
'''num1=int(input('enter a number: '))
rev=0
temp=num1
while num1>0:
      digit=num1%10
      rev=rev*10+digit
      num1//=10
if temp==rev:
      print('palindrome')
else:
      print('not a palindrome')'''

#count digit in number
'''num2=int(input('enter a number: '))
count=0
while num2>0: #123
      num2//=10
      count+=1
print('number of digits :',count)'''

#find the largest digit in a given number
'''num3=int(input('enter a number: '))
largest=0
while num3>0:
      digit=num3%10 #985
      if digit>largest:
            largest=digit
      num3//=10 
print('largest digit is: ',largest) '''

#print fibonocci series
'''n=10 # can also take user input
a,b=0,1
i=0
while i<n:
      print(a, end=' ')
      a,b=b,a+b
      i+=1'''

#armstrong number
'''num=574
arm=0
while num>0:
      digit=num%10
      sqr=digit*digit
      arm+=sqr
      num//=10
print(arm)'''

        


