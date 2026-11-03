# LeetCode 271. Encode and Decode Strings (NeetCode 150)
# https://leetcode.com/problems/encode-and-decode-strings/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(m)  Space: O(m)  (m = total characters across all strings)
# Insight:
#   - Why length-prefixing works: each string is stored as "<len>$<string>". The length
#     digits never contain "$", so the first "$" at or after i is always the delimiter,
#     and then exactly len characters are read. The string itself can contain "$",
#     digits or be empty without breaking anything, unlike joining on a separator.
#   - [AVOID COPY] Improved from the first version: no leading count of strings (decode
#     just loops until the end of s), and no s = s[ptr:] re-slicing each iteration, which
#     copied the remaining string every time (O(m^2) overall). s.index("$", i) searches
#     from an offset instead, so decode is a single O(m) pass.
#   - [PYTHONIC] "".join(parts) builds the string once, instead of += in a loop.
#   - [PYTHONIC] f"{len(s)}${s}" instead of str(len(s)) + "$" + s.
#   - [PYTHONIC] Alternative: encode is a one-liner with a generator:
#         return "".join(f"{len(s)}${s}" for s in strs)
#   - [BUILT-IN] Alternative: json.dumps(strs) and json.loads(s) handle the escaping.

class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}${s}")  # PYTHONIC: f-string
        return "".join(parts)  # PYTHONIC: join once, no += in a loop

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter = s.index("$", i)  # AVOID COPY: search from offset i, no s = s[ptr:]
            length = int(s[i:delimiter])
            start = delimiter + 1
            result.append(s[start:start + length])
            i = start + length  # AVOID COPY: advance the index, don't re-slice s
        return result
