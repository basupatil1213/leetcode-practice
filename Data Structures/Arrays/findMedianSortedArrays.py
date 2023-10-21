'''
4. Median of Two Sorted Arrays

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


Solution:

This is not the optimum solution, but the approach I have taken here is to first create an array which stores the sorted array created using two passed array and then find the median of the sorted array. 
if the array size is odd then return the middle element or if the array size is even then return the sum of two middle elements divided by two.
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        sortedArray = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sortedArray.append(nums1[i])
                i += 1
            else:
                sortedArray.append(nums2[j])
                j += 1

        # Add the remaining elements from nums1 and nums2
        sortedArray += nums1[i:]
        sortedArray += nums2[j:]
        
        if len(sortedArray)%2 != 0:
            return sortedArray[(len(sortedArray)-1)//2]
        else:
            finalVal = sortedArray[(len(sortedArray)-1)//2] + sortedArray[((len(sortedArray)-1)//2)+1]
        return finalVal/2


sc = Solution

print(f'Median of sorted arrays is: {sc.findMedianSortedArrays(sc, [1,3],[2,4])}')