'''

Problem Statement :-

1910. Remove All Occurrences of a Substring
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
 

Constraints:

1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.

Solution approach:
The approach here is; we are running while loop until substring is present in s and if present
we are finding the start index of substring and splitting string to remove substring and repeating
same step until the main string doesn't contain substring anymore

Time Complexity: O(m*n)
Space Complexity: O(1) as we are not creating any new array or string
Time taken on leetcode: 39ms Beats 71.21%of users with Python3
Space Taken on leetcode : 16.37MB Beats 46.21%of users with Python3
'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # si = len(part)
        # while part in s:
        #     i = s.find(part)
        #     s = s[:i] + s[i+si:]
        #     print(f's is now {s} and length is {len(s)}')
        subStrLen = len(part)
        while(1):
            i = s.find(part)
            if i == -1:
                break
            else:
                s=s[:i]+s[i+subStrLen:]
        return s


sc = Solution
print(f' final output after removing the substring is: {sc.removeOccurrences(sc, "abcasbabaabcasasdabacbc","abc")}')