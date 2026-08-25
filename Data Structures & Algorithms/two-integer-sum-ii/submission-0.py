class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p: int = 0
        q: int = len(numbers)-1

        result: List[int] = []
        while p < q:
            diff = (numbers[p] + numbers[q]) - target
            if diff > 0:
                q -= 1
            elif diff < 0:
                p += 1
            else:
                result = [p+1, q+1]
                break
        
        return result