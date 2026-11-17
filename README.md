# LeetCode Solutions

My LeetCode solutions, organized by pattern. Harder problems include a short note on the key insight.

## Index

| # | Problem | Pattern | Difficulty | Time | Space |
|---|---------|---------|------------|------|-------|
| 1 | [Two Sum](arrays-hashing/1-two-sum.py) | arrays-hashing | Easy | O(n) | O(n) |
| 3 | [Longest Substring Without Repeating Characters](sliding-window/3-longest-substring-without-repeating-characters.py) | sliding-window | Medium | O(n) | O(min(n, m)) |
| 11 | [Container With Most Water](two-pointers/11-container-with-most-water.py) | two-pointers | Medium | O(n) | O(1) |
| 15 | [3Sum](two-pointers/15-3sum.py) | two-pointers | Medium | O(n^2) | O(1) |
| 36 | [Valid Sudoku](arrays-hashing/36-valid-sudoku.py) | arrays-hashing | Medium | O(1) | O(1) |
| 49 | [Group Anagrams](arrays-hashing/49-group-anagrams.py) | arrays-hashing | Medium | O(n * k) | O(n * k) |
| 121 | [Best Time to Buy and Sell Stock](sliding-window/121-best-time-to-buy-and-sell-stock.py) | sliding-window | Easy | O(n) | O(1) |
| 125 | [Valid Palindrome](two-pointers/125-valid-palindrome.py) | two-pointers | Easy | O(n) | O(1) |
| 128 | [Longest Consecutive Sequence](arrays-hashing/128-longest-consecutive-sequence.py) | arrays-hashing | Medium | O(n) | O(n) |
| 167 | [Two Sum II - Input Array Is Sorted](two-pointers/167-two-sum-ii-input-array-is-sorted.py) | two-pointers | Medium | O(n) | O(1) |
| 217 | [Contains Duplicate](arrays-hashing/217-contains-duplicate.py) | arrays-hashing | Easy | O(n) | O(n) |
| 238 | [Product of Array Except Self](arrays-hashing/238-product-of-array-except-self.py) | arrays-hashing | Medium | O(n) | O(1) |
| 242 | [Valid Anagram](arrays-hashing/242-valid-anagram.py) | arrays-hashing | Easy | O(n) | O(1) |
| 271 | [Encode and Decode Strings](arrays-hashing/271-encode-and-decode-strings.py) | arrays-hashing | Medium | O(m) | O(m) |
| 347 | [Top K Frequent Elements](arrays-hashing/347-top-k-frequent-elements.py) | arrays-hashing | Medium | O(n log k) | O(n) |
| 424 | [Longest Repeating Character Replacement](sliding-window/424-longest-repeating-character-replacement.py) | sliding-window | Medium | O(n * m) | O(m) |
| 567 | [Permutation in String](sliding-window/567-permutation-in-string.py) | sliding-window | Medium | O(26 * n) | O(1) |

## Starred (revisit)

Tricky problems to come back to.

| # | Problem | Why it's tricky |
|---|---------|-----------------|
| 424 | [Longest Repeating Character Replacement](sliding-window/424-longest-repeating-character-replacement.py) | The window validity test (length - max frequency <= k), and why a stale `max_freq` is safe in the optimised version. |

## Layout

```
<pattern>/
  <number>-<problem-name>.<ext>
```

Patterns: `arrays-hashing`, `two-pointers`, `sliding-window`, `stack`, `binary-search`,
`linked-list`, `trees`, `heap`, `backtracking`, `graphs`, `dp`, `greedy`, `intervals`, `math-bit`.

## File header template

```
# LeetCode <number>. <Title>
# https://leetcode.com/problems/<slug>/
# Difficulty: Easy | Medium | Hard
# Pattern: <pattern>
# Time: O(?)  Space: O(?)
# Insight: <one or two lines>
```
