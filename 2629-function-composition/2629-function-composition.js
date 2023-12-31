/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {

	return function(x) {
        let init=x;
        for(let i=functions.length-1;i>=0;i--)
        {
           
           init=functions[i](init);

        }
        return init;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */