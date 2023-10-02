/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let count = 0;
    for(let i = 1; i < nums.length; i++){
        if(nums[i] != nums[i-1]){
            nums[i-count] = nums[i];
        }else{
            count++;
        }
    }

    return count;
};