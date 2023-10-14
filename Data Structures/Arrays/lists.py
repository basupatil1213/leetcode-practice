# array methods

# intializing the array

bostonppl = []

# methods to add values into array

# directly assing list of values to the list

bostonppl = ["Shreyas", "Shridhar", "Rakshith","Shreyas"]
print(bostonppl)
# adding values into array using append method, if we don't specify the index it will add value at the end of the list
bostonppl.append("Amit")
print(bostonppl)

# if we want to add elements at specified index we can use insert method

bostonppl.insert(0, "Sudhendra")
print(bostonppl)

# if we want to extend a list by one value or list of values then we can use extend method

bostonppl.extend(["Basavaraj", "Charan"])
print(bostonppl)


#methods to remove elements from array

# if we want to remove last element from an array we can go with pop
bostonppl.pop() # this will return and delete the last element in the array
print(bostonppl)

# if we want to remove element from specified index we can specify the index number inside pop method
bostonppl.pop(2)
print(bostonppl)

bostonppl.pop(-1)#this will also work for negative indices as well
print(bostonppl)

#if you want to remove values by the value you can use remove method which will remove the first occurance of the specified value
bostonppl.remove("Shreyas")

#use clear method if you want to clear the array
bostonppl.clear()
print(bostonppl)


sortingArray = [3,5,2,1,5,9,6,7,8]

# use sort method to sort the array
sortArray= sortingArray.sort()
sortedArray = sorted(sortingArray)  ## another way is using built-in function
print (sortedArray )
print(sortArray)

#use copy method to copy all the elements from one list to another
copyList=[]
copyList= bostonppl.copy()
copyList2 = bostonppl[:] ###another way is using slice operator
print ("copied List:", copyList)
print(copyList2)

# use reverse method to reverse the array
reverseList=sortingArray.reverse()
reverseList2 = sortingArray[::-1] ####another way to reverse the array


#if you want to count the number of elemenths with the specified value use count method
countValue=sortingArray.count(5)
print(countValue)


#if you want to get the index of specified values first occurance use index method
indexValue=sortingArray.index(5)   #####indexing starts at zero so it will give error if not found
