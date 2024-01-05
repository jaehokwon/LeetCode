/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    var num;
    
    for (var i=0; i<nums.length; i++) {
        if (num === undefined || num === null ||
            (nums[i] >= 0 && Math.abs(num) >= Math.abs(nums[i])) ||
            (nums[i] < 0 && Math.abs(num) > Math.abs(nums[i]))) {
            num = nums[i]
        }
    }
    
    return num;
};