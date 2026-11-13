# LeetCode 347. Top K Frequent Elements (NeetCode 150)
# https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(n log k)  Space: O(n)
# Insight:
#   - Why a min-heap capped at size k: popping whenever it exceeds k evicts the
#     smallest count, so what remains is the k most frequent. Each push/pop costs
#     O(log k), not O(log n), so this beats sorting every count.
#   - (count, num) tuples compare by count first, so the heap orders by frequency
#     without needing a key function.
#   - defaultdict(int) removes the "if num not in counter" check when counting.
#   - counter.items() gives the key and value together.
#   - Alternative: collections.Counter does the counting in C, and most_common(k)
#     returns the top k (it uses heapq.nlargest internally, so the same O(n log k)):
#         return [num for num, _ in Counter(nums).most_common(k)]
#   - Alternative: bucket sort for O(n). A count can't exceed len(nums), so use
#     buckets[count] = [nums with that count], then read the buckets from the
#     highest index down until k numbers are collected:
#         buckets = [[] for _ in range(len(nums) + 1)]
# Interview Q&A:
#   Q: Compare the heap, bucket sort and full sort.
#   A: Heap: O(n log k) time. Bucket sort: O(n) time, since counts can't exceed n. Sorting
#      every count: O(n log n). All use O(n) space for the counter.
#   Q: Why a min-heap of size k and not a max-heap?
#   A: Evicting the smallest keeps only k entries, and each operation costs O(log k). A
#      max-heap of everything also works (heapify O(n), k pops), but holds all entries.
#   Q: How are ties handled?
#   A: Tuples compare by count first, then the number. The problem guarantees a unique answer.
#   Q: What if the data is a stream?
#   A: Keep a running counter and heap, or use Misra-Gries / count-min sketch for approximate
#      heavy hitters in bounded memory.

import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        counter = defaultdict(int)
        for num in nums:
                counter[num]+=1
        for num, count in counter.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [num for count, num in min_heap]
