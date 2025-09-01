#basic print function in python
print('sindhu')  #sindhu
name='sindhudodmane'
print(name) #sindhudodmane
print('python', 'is', 'fun') # python is fun
print('python', 'is', 'fun', sep='*') #python*is*fun

# by using string farmat
name = "Sindhu"
score = 95
print("{} scored {} marks.".format(name, score)) #Sindhu scored 95 marks.
print(f"{name} scored {score} marks.") #Sindhu scored 95 marks.

# escape characters inside print fuction
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space
print("She said, \"Python is fun!\"")  # Quotes inside string

print(r'this is \n newline') #raw string to ignores newline 
#a=10
#b=3
#can also assign like this 
a,b =10,3
print(a+b)  #addition , 13
print(a-b)  #subtraction , 7
print(a*b)  #multiplication, 30
print(a/b)  #division, 3.3333333333335
print(a//b)  #floor division, 3
print(a%b)  #modulus ,1
#datatypes and typecast
name='sindhu'
x=20
p=None #special datatype
print(type(a))
y=float(a)
print(type(y))  #checking type of variable
z=str(y)
print(type(z))
print(type(p))
a=True+True+True
print(a) #3

