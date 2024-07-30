"""_summary_

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

def longestSubstring(s: str) -> int:
    seen = {}
    left = 0
    output = 0
    for right in range(len(s)):
        if s[right] not in seen:
            output = max(output, right-left+1)
        else:
            if seen[s[right]] < left:
                output = max(output, right-left+1)
            else:
                left = seen[s[right]] + 1
        seen[s[right]] = right
   
    return output

string = "abcabc"
print(longestSubstring(string))