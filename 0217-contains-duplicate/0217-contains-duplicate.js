/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hashmap={}
    for(let i of nums)
        {
         if (i in  hashmap)
            {
                return true
            }
            hashmap[i]=1
            
        
        }
    return false
};