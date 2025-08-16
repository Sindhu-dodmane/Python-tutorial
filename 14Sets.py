#creating set ,set is unordered and unindexing
my_set={1,2,3,'blue',2} # does not contain duplicate elements
fruits=set(('apple','banana','orange'))
print(my_set)
print(fruits)
#fruits[1]={'banana'} can't support assignment operator
set1={'sindhu',} #to create set with single element
'''to create empty set
dogs={} #this will create an empty dictionary
print(type(dogs)) #dict  '''

new_set=set() #creates empty set called new_set
print(type(new_set))  # <class 'set'>


#3 main operations in set
s1={1,2,6,4,5,6}
s2={'a','b',0.2,3,4,1,0.7}

#union , can also use s1.union(s2)
print(s1|s2) 
#intersection
print(s1&s2)  # {1, 4}
print(s1.intersection(s2)) #can also use
#difference , can also use s2.difference(s2)
print(s2-s1)

#methods
s1.add(4) #already in set does not make any difference
s1.add(.4)  
print(s1)   # {0.4, 1, 2, 4, 5, 6}
s1.remove(6) 
s1.pop() #remove  arbitary element(last)and return
print(s1)   # {0.4, 1, 2, 4, 5}
#s1.remove(10)  # 10 is not present in s1 therefore it rise error to overcome this error we use discard
s1.discard(10)  

#subset and superset
set1={1,2,3,4,5}
set2={1,2,3,4,5,6}
print(set1.issubset(set2)) #true
print(set2.issuperset(set1)) #true
print(set1.issuperset(set2)) #false

# add more elements to set
set2.update((7,8,9)) # put tuple or list as argument for update it will add elements to set
print(set2)

# isdisjoint() method return true if sets have no element in common
print(set1.isdisjoint(set2)) # set1 and set2 are unique so it returns false

#to return the symmetric-difference ,can also use ^
print(set1.symmetric_difference(set2)) #{6,7,8,9} 

print(set1==set2) #false


