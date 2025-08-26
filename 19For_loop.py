'''for loop is used when we now the number of iteration
for condition:
    <block of code'''

#print 1 to 10 using for loop
'''for i in range(1,11): #range(start,end-1,step)
    print(i,end=' ') 
print('\n')
#by using step can print odd numbers
for i in range(1,50,2):
    print(i,end=' ')'''
    
#print square number from 1 to 10
for i in range(1,11):
    print(f'square of {i}={i*i}')

string=input('enter a string: ')
for ch in string:
    print(ch,end=',')
