#reverse of number, remember str slicing
num=int(input('Enter a number: '))
print(num)
rev= str(num)[::-1]
print(rev)
print(type(rev))
#check whether palindrome or not
''' num1=input('enter a number: ')
if num1==num1[::-1] :
    print('palindrome')
else:
  print('not palindrome') '''

if num==int(rev):
    print('palindrome')
else:
    print('not palindrome')