#include <string>
#include <algorithm>

class Solution {
public:
    int numberOfSubstrings(std::string s) {
       
        int abc[3] = {-1, -1, -1};
        int count = 0;

        
        for (int i = 0; i < s.length(); ++i) {
          
            if (s[i] == 'a') {
                abc[0] = i;
            } else if (s[i] == 'b') {
                abc[1] = i;
            } else if (s[i] == 'c') {
                abc[2] = i;
            }

            // Check if all 'a', 'b', and 'c' are found
            if (abc[0] != -1 && abc[1] != -1 && abc[2] != -1) {
                
                count += 1;
           
                int Min = std::min({abc[0], abc[1], abc[2]});
             
                count += Min;
            }
        }

        return count;
    }
};
