# LeetCode 3. Longest Substring Without Repeating Characters (NeetCode 150)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Pattern: sliding-window
# Time: O(n)  Space: O(min(n, m))  (m = size of the character set)
# Insight:
#   - Why it works: the window [left, right] never contains a repeat. char_map stores the
#     last index of every character. When the current character was last seen inside the
#     window (char_map[char] >= left), left jumps straight past that earlier copy, instead
#     of moving one step at a time.
#   - The char_map[char] < left check ignores stale entries: a character last seen before
#     the window isn't a repeat. That's why entries never need deleting.
#   - max_length isn't updated in the else branch: after the jump, the window is no longer
#     than the one before it, so it can't be a new maximum.
#   - Vs the naive approach: checking every substring for repeats is O(n^2) or worse.
#   - Conventional version: keep a set of the window's characters and shrink from the left
#     one character at a time. Still O(n), since each character is added and removed at
#     most once.
#         seen = set()
#         left = 0
#         for right, char in enumerate(s):
#             while char in seen:
#                 seen.remove(s[left])
#                 left += 1
#             seen.add(char)
#             max_length = max(max_length, right - left + 1)
#   - [PYTHONIC] enumerate(s) gives the index and character together.
#   - [PYTHONIC] Shorter form with dict.get and max, with no stale-entry branch:
#         last = char_map.get(char, -1)
#         left = max(left, last + 1)
#         max_length = max(max_length, right - left + 1)
#         char_map[char] = right
# Interview Q&A:
#   Q: The set version has a while loop inside a for loop. Why is it O(n)?
#   A: Each character enters the set once and leaves at most once, so there are at most 2n
#      steps in total.
#   Q: What is the space complexity?
#   A: O(min(n, m)): the map holds at most one entry per distinct character, bounded by both
#      the string length and the character set size. For ASCII, a 128-slot array also works.
#   Q: How would you return the substring itself?
#   A: When max_length improves, record the start index (left) and slice s[start:start + max_length].
#   Q: What if you allow at most k distinct characters (LeetCode 340)?
#   A: Keep character counts in a dict and move left while there are more than k distinct keys.
#   Q: What is the answer for an empty string?
#   A: 0, since the loop never runs and max_length starts at 0.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_map = {}
        left = 0
        for right, char in enumerate(s):
            if char not in char_map or char_map[char] < left:
                max_length = max(max_length, right - left + 1)
            else:
                left = char_map[char]+1
            char_map[char] = right
        return max_length
