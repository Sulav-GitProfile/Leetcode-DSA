class Solution(object):
    def threeSumClosest(self, nums, target): 
        nums.sort()
        l = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(l-2):
            right = l-1
            left = i+1
            while(left<right):
                total = nums[i] + nums[left] + nums[right]
                if(abs(target-total)<abs(target-closest)):
                    closest = total
                if(total>target):
                    right -=1
                elif(total<target):
                    left +=1
                else:
                    return total
        return closest
    
        

      