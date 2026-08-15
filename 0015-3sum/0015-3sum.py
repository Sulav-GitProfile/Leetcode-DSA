class Solution(object):
    def threeSum(self, nums):
        w = len(nums)
        h = max(nums)
        s = min(nums)
        if(w<=3000 and w>=3 and h<=10**5 and s>=-10**5):
            nums.sort()
            og=[]
            for i in range(0,w):
                right = w-1
                left = i+1
                while(left<right):
                    sum = nums[i] + nums[right] + nums[left]
                    if(sum==0):
                        d = [nums[i],nums[right],nums[left]]
                        if(d not in og):
                            og.append(d)
                        right -=1
                        left +=1
                    elif(sum<0):
                        left+=1
                    else:
                        right -=1
            return og


