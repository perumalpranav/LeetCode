import java.util.Arrays;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] onums = nums.clone();
        Arrays.sort(nums);
        int i = 0;
        int j = onums.length-1;
        while(i != j) 
        {
            int small = nums[i];
            int big = nums[j];
            if(small + big == target) 
            {
                System.out.println(small + " " + big);
                return origIndices(onums,small,big);
            }
            else if(small + big < target)
            {
                i++;
            }
            else if(small + big > target)
            {
                j--;
            }
        }
        return null;
    }

    public int[] origIndices(int[] array, int num1, int num2) {
        System.out.println(array[0] + " " + array[1]);
        int[] sol = {-1,-1};
        for(int i = 0; i < array.length; i++) {
            if(array[i] == num1 && sol[0] == -1) {
                sol[0] = i;
            }
            else if(array[i] == num2 && sol[1] == -1) {
                sol[1] = i;
            }
            if(sol[0] != -1 && sol[1] != -1) {
                break;
            }
        }
        return sol;
    }
}