class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0]*len(height)
        rmax = [0]*len(height)

        lm = 0
        rm = 0
        
        for i in range(len(height)):
            lmax[i] = lm
            if height[i] > lm:
                lm = height[i]
            rmax[len(height)-1-i] = rm
            if height[len(height)-1-i] > rm:
                rm = height[len(height)-1-i]
        
        tw = 0
        for i in range(len(height)):
            wt = min(lmax[i], rmax[i]) - height[i]
            if wt > 0:
                tw += wt
        
        return tw
    

