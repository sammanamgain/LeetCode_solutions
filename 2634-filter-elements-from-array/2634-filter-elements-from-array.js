/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr=[];
    const truth=[];
    for(const i in arr)
    {
        truth.push(fn(arr[i],Number(i)))

    }
    //console.log(truth)
    for (const i in arr)
    {
        
        
        if(truth[i]!==false)
        {
            if(truth[i]!=0)
            {
         filteredArr.push(arr[i])
            }
        }
        
    }
    return filteredArr;

};