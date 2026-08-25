class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            # if smallest remaining number is positive it can never sum to 0
            if nums[i] > 0:
                break

            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            p: int = i + 1
            q: int = len(nums) - 1

            while p < q:
                target = nums[i] + nums[p] + nums[q]

                if target > 0:
                    q -= 1
                elif target < 0:
                    p += 1
                else:
                    result.append([nums[i], nums[p], nums[q]])

                    # skip duplicates for p and q
                    while p < q and nums[p] == nums[p + 1]:
                        p += 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1

                    p += 1
                    q -= 1
        
        return result