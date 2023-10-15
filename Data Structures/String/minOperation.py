'''
    Solution Explanation
    the main intention is to get value from all other places which have non zero positive numbers into the current target place,
    and the constraint is we can move the value from a --> b only if b is beside a which means if i want to pass value from a,d in array
    [a,b,c,d] i need to pass it from a -> b then b -> c and c -> d which means it requires the number of steps which is equals to the distance 
    between the indexes of that number, so just take the count of difference of all the positive number indexes to the target number index
    and add that to list
'''
class Solution:
    def minOperations(self, boxes: str):
        opArray = []
        for i in range(len(boxes)):
            minopno = 0
            for j in range(len(boxes)):
                if int(boxes[j]) != 0:
                    minopno += abs(j-i)
            opArray.append(minopno)
        return opArray

opSol = Solution
print(f' minOperation required for each place: {opSol.minOperations(opSol,"1100101")}')