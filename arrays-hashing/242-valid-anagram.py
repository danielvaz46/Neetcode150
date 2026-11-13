# LeetCode 242. Valid Anagram (NeetCode 150)
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Pattern: arrays-hashing
# Time: O(n)  Space: O(1) (fixed 26-slot array)
# Insight:
#   - Different lengths can never match, so check that first for early stopping.
#   - One pass over both strings: +1 for s, -1 for t. An all-zero array means anagram.
#   - zip(s, t) is the Python way to walk two sequences together, instead of
#     for i in range(len(s)) with s[i] and t[i].
#   - Alternative: collections.Counter counts in C and also handles Unicode
#     (the 26-slot array only works for a-z):
#         return Counter(s) == Counter(t)
# Interview Q&A:
#   Q: What if the strings contain Unicode?
#   A: Replace the 26-slot array with a dict or Counter. Space becomes O(k) for k distinct
#      characters.
#   Q: What about sorting both strings?
#   A: sorted(s) == sorted(t) is O(n log n) time and O(n) space, simpler but slower.
#   Q: Why check the lengths first?
#   A: Different lengths can never be anagrams, and equal lengths make the +1/-1 pass
#      sufficient: an all-zero array means the counts match.
#   Q: Is the space really O(1)?
#   A: Yes for a fixed alphabet. For Unicode it grows with the number of distinct characters.

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        a = ord('a')
        for c1, c2 in zip(s, t):
            counts[ord(c1) - a] += 1
            counts[ord(c2) - a] -= 1

        return not any(counts)
