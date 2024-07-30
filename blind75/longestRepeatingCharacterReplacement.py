"""_summary_
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

def characterReplacement(s: str, k: int) -> int:
    output = 0
    n = len(s)
    for c in range(ord("A"), ord("Z") + 1):
        c = chr(c)
        left, right, replaced = 0, 0, 0
        
        while right < n:
            if s[right] == c:
                right += 1
            elif replaced < k:
                right += 1
                replaced += 1
            elif s[left] == c:
                left += 1
            else:
                left += 1
                replaced -= 1
            output = max(output, right - left)
    return output

string = "AABABBA"
print(characterReplacement(string, 1))
