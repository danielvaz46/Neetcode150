# LeetCode 567. Permutation in String (NeetCode 150)
# https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium
# Pattern: sliding-window
# Time: O(26 * n)  Space: O(1)  (n = len(s2); 26 is the cost of comparing the counts)
# Insight:
#   - Why it works: a permutation of s1 is a substring of s2 with the same length and the
#     same letter counts. Slide a fixed-size window of length len(s1) over s2. Each step adds
#     the incoming letter, drops the letter leaving the window (s2[i - l1]) and compares the
#     two count arrays.
#   - Fixed-size window: its length never changes, so one index i is enough. The letter that
#     leaves is always at i - l1, with no separate left pointer.
#   - Vs the naive approach: counting or sorting every substring from scratch is O(n * m) or
#     O(n * m log m) (m = len(s1)). Updating the counts one letter in, one letter out makes
#     each step O(1) before the comparison.
#   - Comparing two 26-slot lists is a constant-size cost, so the total is O(26 * n), which is
#     O(n) for a fixed alphabet.
#   - [PYTHONIC] c1 == c2 compares two lists element by element.
#   - [PYTHONIC] ord(ch) - base maps a letter to a 0-25 index, as in 242.
#   - [BUILT-IN] Alternative: Counter on every window. Shortest, but it recounts each
#     window from scratch, so it is O(n * m):
#         return any(Counter(s2[i:i + l1]) == Counter(s1) for i in range(len(s2) - l1 + 1))
# Interview Q&A:
#   Q: Why compare letter counts instead of sorting each window?
#   A: Sorting each window costs O(m log m). Counts update in O(1) as the window slides, and
#      equal counts is exactly what "permutation" means.
#   Q: What are the complexities?
#   A: O(26 * n) time, which is O(n) for a fixed alphabet, and O(1) space for two 26-slot arrays.
#   Q: Why does the removal happen only when i >= l1?
#   A: Up to index l1 - 1 the window is still filling. From i = l1 on, it would hold l1 + 1
#      letters, so the letter at s2[i - l1] must leave.
#   Q: What if s1 is longer than s2?
#   A: It returns False. The window never reaches len(s1) letters, so the counts can't match.
#   Q: How would you return every start index (LeetCode 438, Find All Anagrams)?
#   A: Same window, but append i - l1 + 1 whenever the counts match instead of returning True.
#   Q: What if the alphabet isn't a-z?
#   A: Use dicts or Counters instead of the 26-slot arrays. Comparing them then costs
#      O(distinct letters) rather than a fixed 26.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0]*26
        l1 = len(s1)
        c2 = [0]*26
        base = ord("a")
        for ch in s1:
            c1[ord(ch) - base] += 1
        for i, char in enumerate(s2):
            c2[ord(char) - base] += 1
            if i >= l1:
                c2[ord(s2[i-l1]) - base]-=1
            if c1 == c2:
                return True
        return False
