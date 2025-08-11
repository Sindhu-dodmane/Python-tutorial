#basic print function in python
print('sindhu')
name='sindhudodmane'
print(name)
print('python', 'is', 'fun')
print('python', 'is', 'fun', sep='*')

# by using string farmat
name = "Sindhu"
score = 95
print("{} scored {} marks.".format(name, score))
print(f"{name} scored {score} marks.")

# escape characters inside print fuction
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space
print("She said, \"Python is fun!\"")  # Quotes inside string

print(r'this is \n newline') #raw string to ignores newline 
#a=10
#b=3
#can also assign like this 
a,b =10,3
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a//b)  #floor division
print(a%b)  #modulus
#datatypes and typecast
name='sindhu'
x=20
p=None #spl datatype
print(type(a))
y=float(a)
print(type(y))  #checking type of variable
z=str(y)
print(type(z))
print(type(p))


