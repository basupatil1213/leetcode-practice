
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