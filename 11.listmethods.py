# list methods
fruits=['banana','cherry','apple','kiwi']
sindhu=[1,2,3,4,5,4,3,5,63,2]
print(fruits.reverse()) # does not return a value return null
print('length of list is: ',len(sindhu)) # returns number of items in list
print(sorted(sindhu)) #returns sorted list
# print(sort.sindhu) because it does not return list so 1st sort then print
sindhu.sort()
print(sindhu)
print('sum of items in list is: ',sum(sindhu))
#print(sum(fruits)) TypeError: unsupported operand type(s) for +: 'int' and 'str'
print( 'count of 2 is: ',sindhu.count(2))
print('index of 63 is: ',sindhu.index(63))
sindhu.reverse()
print(sindhu)


#some special about list
import copy
a=[1,2,3]
b=a[::]     #shallow copy
c=copy.deepcopy(a) #deep copy
print(b,c)

#reverse list without reverse and slicing
def reverse(a):
    result=[]
    for i in a:
        result=[i] +result
    return result

#min and max element in list
print(min(a))
print(max(a))
