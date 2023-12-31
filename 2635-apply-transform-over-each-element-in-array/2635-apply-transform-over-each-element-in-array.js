/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const returnedArray=new Array(arr.length);
    for (const i in arr)
    {
        returnedArray[i]=fn(arr[i],Number(i))
    }
    return returnedArray;

};

//map([1,2,3],plusone)


//or
// for(const i  in arr)
//{

//}