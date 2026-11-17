# LeetCode 424. Longest Repeating Character Replacement (NeetCode 150)
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium
# Pattern: sliding-window
# Time: O(n * m)  Space: O(m)  (m = alphabet size, 26 here, so effectively O(n))
# Insight:
#   - Why it works: a window can be turned into one repeated letter with at most k
#     replacements iff (window length - count of its most frequent letter) <= k. Keep the
#     most frequent letter and replace the rest. Always grow the window on the right, and if
#     it needs more than k replacements, shrink from the left until it is valid again. The
#     answer is the largest valid window seen.
#   - max(f_map.values()) rescans the counts every check, but there are at most 26 keys,
#     so that scan is constant size. A larger alphabet would make it cost O(m) per check.
#   - Vs the naive approach: checking the most frequent letter of every substring is O(n^2)
#     or worse.
#   - Optimised version: keep max_freq as a running variable that only ever increases,
#     and use if instead of while. The window then never shrinks, it only slides, so the
#     answer is its final size. A stale (too high) max_freq can only stop the window growing,
#     never push it past the best valid size, so the result stays correct. O(n) for any alphabet.
#         max_freq = 0
#         for right, char in enumerate(s):
#             f_map[char] += 1
#             max_freq = max(max_freq, f_map[char])
#             if (right - left + 1) - max_freq > k:
#                 f_map[s[left]] -= 1
#                 left += 1
#         return len(s) - left
#   - [PYTHONIC] defaultdict(int) removes the missing-key check when counting.
#   - [PYTHONIC] max(f_map.values()) takes the largest count directly.
#   - [BUILT-IN] collections.Counter() works as a drop-in for defaultdict(int) here.
# Interview Q&A:
#   Q: Why is (window length - max frequency) the number of replacements needed?
#   A: Keep the most frequent letter and replace every other letter in the window.
#   Q: Is recalculating max(f_map.values()) every time too slow?
#   A: Not here: the input is uppercase letters only, so it scans at most 26 counts, which makes
#      it O(26 * n) = O(n). With a large alphabet it would be O(n * m).
#   Q: How do you avoid the scan?
#   A: Track max_freq as a running maximum that never decreases (the optimised version above).
#   Q: Why is a stale max_freq safe?
#   A: The window only grows when a letter's real count in the window beats the old max.
#      Otherwise it just slides, and the final size is still the best valid window.
#   Q: What is a related problem?
#   A: Max Consecutive Ones III (LeetCode 1004): the longest window with at most k zeros.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f_map = defaultdict(int)
        left = 0
        max_l = 0

        for right, char in enumerate(s):
            f_map[char]+=1
            l = right - left + 1
            while l - max(f_map.values()) > k:
                f_map[s[left]]-=1
                left += 1
                l = right-left + 1
            max_l = max(max_l, l)
        return max_l
