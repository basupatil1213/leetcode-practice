# tuples are immutable/unchangable

# Create a tuple
my_tuple = 1,2,3,4,5,"without paranthses" # parentheses or not doesn't matter.
my_tuple2 = (6,7,8,9,"with paranthses")
print(my_tuple)
print(my_tuple2)

#get the value from index
print("index: ", my_tuple[0])

#use count to get the count of the element
print('count:', my_tuple.count(1))