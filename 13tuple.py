a=int('20',8)
b=int('0b100',base=0)
print(a,b)

my_tuples=('sindhu',2)
print(my_tuples)
# if u want to create single element in tuple
my_tuple=(2,)
print(type(my_tuples))    # type of tuple
print(my_tuples[0])         #indexing
print(len(my_tuples))        #length


# my_tuples[0]='bindhu'  if you want change item in tuple it will rise 
# TypeError: 'tuple' object does not support item assignment because tuple are immutable
# we can't add item to tuple directly we can covert tuple into list then append again 
#convert into tuple

my_tuple = (1, 2, 3)
temp_list = list(my_tuple)   # Convert to list
temp_list[1] = 20           # Modify
my_tuple = tuple(temp_list) # Convert back

print(my_tuple)  # (1, 20, 3)


# rebuild the tuple
my_tuple = (1, 2, 3)
my_tuple = (my_tuple[0], 20, my_tuple[2])
print(my_tuple)  # (1, 20, 3)

# if tuple contain mutable object
my_tuple = ([1, 2, 3], 4, 5)
my_tuple[0][1] = 20
print(my_tuple)  # ([1, 20, 3], 4, 5)

#by slicing
my_tuple = (1, 2, 3, 4, 5)

# Let's say we want to change the item at index 2 (the value 3) to 30

index_to_change = 2
new_value = 30

# Rebuild tuple by slicing up to index, add new value, then add rest of tuple after index
my_tuple = my_tuple[:index_to_change] + (new_value,) + my_tuple[index_to_change + 1:]

print(my_tuple)
# Output: (1, 2, 30, 4, 5)

#tuple concatenation and replication & membership operator

print(my_tuple+my_tuple)
print(my_tuple*3)

print(4 in my_tuple)






