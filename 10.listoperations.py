#adding elements to list
my_list=[10,20,30,40,10,30]
my_list.append(80) #appends elemets at the end
my_list.insert(2,60) #insert at specific index
my_list.extend([1,2,3,4]) #extends the list with another list
print(my_list)

#removing the elements
my_num=[1,2,3,4,5,3]
my_num.remove(2) # removes specific element
my_num.remove(3) #removes first occurnce
my_num.clear() #deletes all the elements but returns empty list
print(my_num)
numbers=[11,12,13,14]
print(numbers)
del numbers[1]
print(numbers)
del numbers
# print(numbers) rise error because del numbers completely delete the list.

num1=['a','s','d','f','g']
num1.pop() # deletes last item
num1.pop(3) #can also specify index
print(num1)

#slicing
print(my_list[2::3])
print(my_list[2:5:-1]) #wn -ve slicing start index must be grater than the stop index.
# here viseversa it is impossible to backward form index 2 to 5 so,return empty list