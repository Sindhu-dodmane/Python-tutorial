#Dictionaries datastructure stores the elements as key-value pair
# it is mutable.
my_dict={"sindhu":'20-09-2003',
        'kishor':'21-09-2001',
        'john':'20-02-2011'}
meaning=dict({'A':'Apple','B':'Ball'})
print(my_dict)
print(meaning)
print(type(my_dict)) #<class:dict>

#access the elements by key value
print(my_dict['kishor']) # 21-09-2003
#if key is not present it will return error so we will use get() method
print(my_dict.get('bindhu','not found')) # 'bindhu' is not present in my_dict so it will return 'not found'
print(my_dict.get('dog')) #None

#modify dictionary
# add and update
my_dict['kishor']='23-09-2001'  #updating
my_dict['baanu']='01-01-2000'   #adding
print(my_dict) 

#delete the elements
my_dict.pop('kishor') # del my_dict['kishor'] this will also work but does not support assignment operator
y=my_dict.pop('john')
print(y)  #20-02-2011
print(my_dict)
# meaning.clear()  delete dictionary called 'meaning'

#methods
print(my_dict.keys(),my_dict.values())
print(my_dict.items()) #print each element as tuple
my_dict.update(meaning)
print(my_dict) #my-dict updated with elemets of dict 'meaning'

#tuple can be used as keys  as well as values in dictionary and list can be used as value
dict1={(1,2,3):6, 4:(2,2),6:[2,3]}
print(dict1)

item1={
    'name':'milk',
    'weight':1,
    'price':'50'
}
item2={
    'name':'sugar',
     'weight':2,
     'price':99.9
}
items=[item1,item2]
print(items)
print(f'total weight:{item1["weight"] + item2["weight"]}kg')

#nested dictionary  / list of dictionaries
itemss=[{
    'name':'milk',
    'weight':1,
    'price':'50'
},
{
    'name':'sugar',
     'weight':2,
     'price':99.9
}]
print(itemss)

#membership operator
print('sindhu' in my_dict) #true
print('sneha'not in my_dict) #true
print('baanu' not in my_dict) #false

di={1:2,2:1,1:3}
print(di)  # {1: 3, 2: 1} no duplicate key , latest value overwritten the old one
print(di.popitem())  #remove last inserted key-value pair

# covert two list into dictionary
keys=['name','id','age']
values=['sindhu',27,20]
converted=dict(zip(keys,values))
print(converted)

#Dictionary Comprehension
squares={x: x*x for x in range(5)}
print(squares) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

s = "pythonprogramming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)