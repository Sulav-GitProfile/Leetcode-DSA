

class Solution {
    public int[] twoSum(int[] nums, int target) {
        boolean found =false;
        for(int i=0; i<nums.length; i++){
            for(int j=0; j<nums.length; j++){
                if (i==j){
                    continue;
                }
            int sum = nums[i]+nums[j];
            if(sum==target){
                found = true;
                return new int[]{i,j};
            }
            }
         }
           return null;
        
}
}

// Sulav Tiwari
public class Main{
    public static void main(String []args){
        int [] arra = {2,7,11,15};
        int targ = 9;
       Solution c = new Solution();
       c.twoSum(arra, targ);

    }
}



       
