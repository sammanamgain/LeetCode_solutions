/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache={}
    
    return function(...args) {
        stringkey=JSON.stringify(args)
        if(stringkey in cache)
            {
                return cache[stringkey]
            }
        
        cache[stringkey]=fn(...args)
        return cache[stringkey]
        
    }
}
//this is the example of caching

/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */