# LeetCode 49. Group Anagrams (NeetCode 150)
# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(n * k)  Space: O(n * k)  (n = number of words, k = longest word)
# Insight:
#   - Lists aren't hashable, so convert the counts to a tuple to use it as a dict key.
#   - defaultdict(list) removes the "if key not in groups" check before appending.
#   - for char in word iterates the characters directly, no range(len(word)).
#   - Alternative: key on tuple(sorted(word)) or "".join(sorted(word)). Much shorter,
#     but O(k log k) per word instead of O(k). Fine for short words, and also handles
#     Unicode (the 26-slot counts only work for a-z).
#   - Counter(word) can't be a key directly (dicts aren't hashable), but
#     frozenset(Counter(word).items()) works.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        a = ord('a')
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - a] += 1
            groups[tuple(counts)].append(word)
        return list(groups.values())
