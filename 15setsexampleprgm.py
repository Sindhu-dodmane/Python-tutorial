print(set('python')) # {'h', 'n', 'y', 'o', 'p', 't'}
s1={'python',} 
print(s1)  #{'python'}

# frozenset() used to create immutable set
set1=frozenset((1,2,3,4,5)) #pass list or tuple
print(set1,type(set1))  #frozenset({1,2,3,4,5})
# set1[1]={0} or set1.add(7) 'frozenset' object does not support item assignment and it is immuatable
set2={1,2,3,4,5,6,7}
# noindexing in set so accessing element in list by loop
for item in set2:
    print(item)

#remove duplicates from a list using a set
list1=[1,2,3,4,2,4,5]
unique=list(set(list1))
print(unique)

#convert string to set
fruit='banana'
fruits=set(fruit)
print(fruits)


