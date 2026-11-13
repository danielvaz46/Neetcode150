# LeetCode 125. Valid Palindrome (NeetCode 150)
# https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Pattern: two-pointers
# Time: O(n)  Space: O(1)
# Insight:
#   - Why it works: a palindrome mirrors around its centre, so compare the outermost
#     characters and move inward. Each pointer skips non-alphanumeric characters first,
#     and the left < right guard in the inner loops stops them crossing (an empty or
#     all-punctuation string falls through and returns True).
#   - Vanilla: build a cleaned, lowercased copy and compare it to its reverse. Same
#     O(n) time, but O(n) extra space and the full string is always built. Two
#     pointers work in place and return False at the first mismatch.
#   - [PYTHONIC] left, right = 0, len(s) - 1 sets both pointers in one line.
#   - [PYTHONIC] isalnum() covers letters and digits, so no manual character ranges.
#   - [BUILT-IN] Alternative: clean and compare to the reverse (O(n) space):
#         cleaned = "".join(c.lower() for c in s if c.isalnum())
#         return cleaned == cleaned[::-1]
#   - [BUILT-IN] How slicing works: seq[start:stop:step]. start is included, stop is
#     excluded, and any part can be left out. A positive step walks left to right
#     (defaults: start=0, stop=len). A negative step walks right to left (defaults:
#     start=last index, stop=past the first), so [::-1] copies the sequence backwards.
#     Slicing always builds a new copy (O(n) space); reversed(s) is a lazy iterator.
#         "abcdef"[::-1]    -> "fedcba"   every item, backwards
#         "abcdef"[::2]     -> "ace"      indices 0, 2, 4
#         "abcdef"[1::2]    -> "bdf"      indices 1, 3, 5
#         "abcdef"[::-2]    -> "fdb"      indices 5, 3, 1
#         "abcdef"[4:1:-1]  -> "edc"      indices 4, 3, 2 (stop 1 is excluded)
# Interview Q&A:
#   Q: Why is two pointers better than reversing a cleaned copy?
#   A: Both are O(n) time, but pointers use O(1) space and stop at the first mismatch.
#   Q: What about Unicode and accents?
#   A: isalnum() works on Unicode letters. casefold() is a safer case-insensitive match than
#      lower() (e.g. German ss), and unicodedata.normalize handles accent forms.
#   Q: How would you allow deleting one character (LeetCode 680)?
#   A: On the first mismatch, check whether skipping the left or the right character leaves
#      a palindrome. Still O(n).
#   Q: Why does the inner loop check left < right again?
#   A: Without it the pointers can cross or index out of range on strings of only punctuation.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
