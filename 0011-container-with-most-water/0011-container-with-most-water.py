class Solution(object):
    def maxArea(self, height):
        
        n = len(height)
        maxim_area = 0
        left = 0
        right = n-1

        while(left<right):
            h = min(height[left], height[right])
            b = right - left
            Area = h * b 
            if(Area>maxim_area):
                maxim_area = Area
            if(height[left]<=height[right]):
                left+=1
            else:
                right-=1
            
        
        return maxim_area
        