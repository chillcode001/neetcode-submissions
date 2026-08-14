class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx in range(len(nums)):
            if nums[idx] in map.keys():
                return [map[nums[idx]], idx]
            map[target-nums[idx]] = idx
        return []