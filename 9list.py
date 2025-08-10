#create list in 2 ways
my_list=['apple','banana','orange','cherry']
number_list= list((2,30,40,50))
mixed_list=['sindhu',20,'bindu',25]  #remember heterogenious and mutable
print(my_list,'\n',number_list,'\n',mixed_list)

#accessing list through index
print(my_list[2])
print(number_list[-1])
print(mixed_list[0:3])

# list slicing
print(my_list[0::2])
print(number_list[::-1]) #to print in reverse order

#modify list
my_list[0]='banana'
number_list[0:]=[10,20,30,40]
print(my_list)
print(number_list)

#covertlist tostring
games=['cricket','kabaddi','chess','vollyball'] #if list has number it rise error
print(" ".join(games))   #cricket kabaddi chess vollyball
print(','.join(games))  #cricket,kabaddi,chess,vollyball


