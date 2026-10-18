class Solution:
    def maxArea(self, height):
        l=0
        r=len(height)-1
        ans=0
        while l < r:
            h = r - l
            w = min(height[l],height[r])
            ans = max(ans,h*w)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans