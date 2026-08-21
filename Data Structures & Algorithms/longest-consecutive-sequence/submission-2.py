class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        max_seq = 0

        for num in nums:
            if num-1 not in table:
                seq = 1
                while num + seq in table:
                    seq += 1
                max_seq = max(seq, max_seq)

        return max_seq
            