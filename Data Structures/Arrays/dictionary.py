# all dictionary methods

# creating dictonary

# directly assiging key value pair

dict1 = {'name': 'John', 'Age': 24} # keys can be any immutable type. Values are mutable types

print(f'dict1: {dict1}')
keys = ("Shryas", "Shridhar", "Basavaraj")

# if we have a set of keys and want to intialize all the keys with same value then we can use fromKeys which takes list of keys as first param and single value as second param
dict2 = dict.fromkeys(keys,24)
print(f'dict2 : {dict2}')

# use defaultDict if you want to initialize with default values

value3 = dict2.setdefault("amit") # we are assigning value of the dict2 with key amit to value3
print(f'dict3: {value3}')
print(f'dict2: {dict2}')

# dict of items returns list of the tuple of key value pair
print(dict2.items())

for key,value in dict2.items():
    print(f'key is {key} and value is {value}')
    
#get method gives the value of give key
print('Value for name:', dict1['name'])

#keys method returns the keys from the dict
print('\nKeys:',dict2.keys())


#use pop to get remove the element with specified key
print("\nPopping Shridhar's age:",dict2.popitem("shridhar"),'\n')

#popitem removes the last inserted key value pair
print("Removing item:",dict2.popitem())


