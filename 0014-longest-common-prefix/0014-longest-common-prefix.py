class Solution(object):
    def longestCommonPrefix(self, strs):
        if(strs[0]=="" or len(strs)==1):
            return strs[0]
        f = strs[0]
        l = len(f)
        w = len(strs)

        strin = ""
       
        req = len(min(strs, key=len))
        for i in range(req):
            for j in range(1,w):
                if(f[i]!=strs[j][i]):
                    strin = f[0:i]
                    return strin
                

        return f[0:req]

        
        
    
  