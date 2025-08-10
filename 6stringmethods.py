#string operation
#concatenation using + operator
num1='  hello! '
num2='Hi'
print(num1+' '+num2)
#replication using * operator
print(3*num1)

#string methods
print(num2.upper()) #convert to uppercase
print(num2.lower())  #to convert into lowercase
print(num2.casefold()) # another method to convert into lowercase
print(num1.strip()) #remove the leading and trailing space
print(num1.lstrip()) # remove left space
print(num1.rstrip()) # remove right space
print(num2.center(100)) # return centered string
print(num1.ljust(1))  # work same as lstrip
print(num1.index('e'))  #index() and find() return idex of specific character
print(num1.find('e'))
print(num1.format()) #works as print()
print(num1.isalnum())
print(num1.isascii())
print(num2.endswith('i'))
print(num1.count('l')) # return count of occarence og same character or substring
print(num1.split('l')) #split the string and return as list
print(num1.swapcase())  #lower to upper and upper to lower
print(num1.title()) #convert first chharacter  of every word to upper case
print(num1.join('si')) #insert the string

print('hello world'.capitalize()) #returns only first letter as capital
print('hello world'.title())  # returns first letter of every word as capital
