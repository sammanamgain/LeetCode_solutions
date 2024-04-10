/**
 * @param {string} s
 * @return {number}
 */
function numberOfSubstrings(s) {
    // Initialize positions of 'a', 'b', and 'c' to -1
    var abc = [-1, -1, -1];
    var count = 0;

    
    for (var i = 0; i < s.length; ++i) {
      
        if (s[i] === 'a') {
            abc[0] = i;
        } else if (s[i] === 'b') {
            abc[1] = i;
        } else if (s[i] === 'c') {
            abc[2] = i;
        }

       
        if (abc[0] !== -1 && abc[1] !== -1 && abc[2] !== -1) {
            // Increment count
            count += 1;
            // Find the minimum position
            var Min = Math.min(abc[0], abc[1], abc[2]);
            // Increment count by the minimum position
            count += Min;
        }
    }

    return count;
}
