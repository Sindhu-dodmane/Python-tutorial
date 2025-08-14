name="sindhu said 'hello'"
print(name)
# we can also use triple quote to print multi line string
name1='''sindhu said "hi" 
        bindu said 'hello' '''
print(name1)

#accesing strings
print(name[1])
print(name[-1]) #negative indexing

#to retrive substring or some portion of string by string slicing
print(name1[0:4])
print(name[::])
print(name[:5]) #spl types
print(name[0:])

#another spl type [start:end:step/skip]
print(name[::2])
print(name[::-1])

#escape characters
print('this is string\n you know')
print('this is string \tyou know')
print('this is string \\you know') #to print backslash
