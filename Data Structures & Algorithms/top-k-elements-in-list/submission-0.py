class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        top_elements = []
        for bucket in reversed(buckets):
            top_elements.extend(bucket)

        return top_elements[:k]