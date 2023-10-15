'''
Problem Statement : leetcode 2405. Optimal Partition of String
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.


Solution:
As per the greedy algorithm we would just traverse across the string and go through each character 
and see if it is repeating, as soon as you see a characer which is repeating u consider the string 
until then as separate string and this one would be new one from now on.
Here we are just updating the counter as we encounter every new string
Time Complexity = O(n) as we are looping through entrie string once
Space Complexity = O(1) as we are not creating any array or string of any size and we have only 
some constant variables

 Time for Execution : Beats 92.04% of users with Python3
 memory Taken: Beats 96.56% of users with Python3
'''


class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        temp =''
        for i in s:
            if i in temp:
                count+=1
                temp = i
            else:
                temp+=i
        return count
    

sc = Solution 
print(f'Count of minimium unique strigs possible : {sc.partitionString(sc, "abacaba")}')