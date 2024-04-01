/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
   
    if (nums.length %2 !=0)
        {
nums.push(0)
        }
  
    let j=1
    for (let i=0;j<=nums.length-1;i=i+2,j=j+2 )
        {
            if (nums[i]!=nums[j])
                {
                    return nums[i]
                }
        }
    return 0

};