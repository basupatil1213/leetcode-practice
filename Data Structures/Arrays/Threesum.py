'''
Problem 15: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Solution approach:
    There are two requirements here
        1. to find the triplets which sums up to 0
        2. make sure the triplets are unique like [-1,0,1] and [0,-1,1] is same this should be mentioned only once
    !!! we are sorting the list at first so that we can find unique pairs and this we are doing by looking at the item
    at present index is same as previous index, if it is same then we already know all the combinations of that numbers
    so we just skip that number and move to next number, we are making it at two places on at top for loop to see if i value
    is same as previous value and one inside while loop to check if left value is same as previous left value
    approach below we have taken is to solve two sum for each iterable value first
    the first for loop loops through the list and for each item when run while loop which checks for the matching 
    two pairs to get sum as 0
'''
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right-=1
                elif threeSum < 0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        return result


sc = Solution
print(f'3 Sum output:  {sc.threeSum(sc,[-1,0,1,2,-1,-4])}')