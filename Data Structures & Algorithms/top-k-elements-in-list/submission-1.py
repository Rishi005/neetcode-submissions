class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq+1)]

        for key, value in counts.items():
            buckets[value].append(key)

        out = []

        for l in buckets:
            out += l
        print(out)
        out = out[::-1]
        return out[:k]
