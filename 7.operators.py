#arithmetic operator
a=10
b=3
print(a+b) #addition, 13
print(a-b) #subtraction, 7
print(a/b) # Division, 3.3333333333335
print(a//b) # Floor division or integer division, 3
print(a*b)  # multiplication, 30
print(a**b) #exponent, 1000

#assignment operators
a=b # a=3 ,b=3
a+=b # a=a+b  so 
print(a) #a=6
a-=b    # a=a-b
print(a)  #a=3
a*=b   #a=a*b
print(a)  #a=9
a/=b    # a=a/b
print(a) #a=3.0
a%=b   #a=a%b
print(a)   #0.0              

#logical operator
print(2<4 and 3<4) # returns true if both expression are true 
print(2<4 or 5<4) #returns true if one of the expression is true
print(not True) #returns compliment of that

#membership operator in and not in
name='i love python'
list=[2,3,4,5]
print('i' in name)
print('love' not in name)
print('sindhu' not in name)
print(6 in list) #print('6' in list)

#comparision operators
print(2==2)   #true
print(2!=2)    #flase
print(2>2)     #flase
print(2<2)       #flase
print(2>=2)     #true
print(2<=2)     #true

#bitwise operators
x,y= 2,4  #x=0010 y=0100
print(x&y) # output 0
print(x|y)  #output 0110 i.e 6
print(x^y)  #output 0110 i.e 6
print(~x)   #output 1011 i.e 11
print(x<<1) #leftshift 
print(x>>1) #right shift

 






