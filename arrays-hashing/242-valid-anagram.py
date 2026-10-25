# LeetCode 242. Valid Anagram (NeetCode 150)
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Pattern: arrays-hashing
# Time: O(n)  Space: O(1) (fixed 26-slot array)
# Insight: Two strings are anagrams iff their character counts match. Different lengths
#          can never match, so check that first. One pass over both strings: +1 for s,
#          -1 for t, and an all-zero array means they're anagrams.
#          zip(s, t) is the Python way to walk two sequences together, instead of
#          for i in range(len(s)) with s[i] and t[i].
#          Alternative: collections.Counter, which counts in C and also handles Unicode
#          (the 26-slot array only works for a-z):
#              return Counter(s) == Counter(t)

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
