/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  return nums.length != new Set(nums).size;
};

var containsDuplicate_v2 = function (nums) {
  nums.sort((a, b) => a - b);

  let occur = 0;
  for (i = 0; i < nums.length - 1; i++) {
    if (nums[i] == nums[i + 1]) {
      occur++;
      return true;
    }
  }
  return false;
};
