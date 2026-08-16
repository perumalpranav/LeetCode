#include <cstdlib>
using namespace std;

class Solution {
public:
    long long splitArray(vector<int>& nums) {
        vector<bool> primes(nums.size(), true);

        long long P = 0;
        long long notP = 0;

        for(int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                notP += nums[i];
            }
            else if (i == 1) {
                notP += nums[i];
            }
            else {
                if (primes[i]) {
                    P += nums[i];
                    for(int j = i + i; j < nums.size(); j+=i) {
                        primes[j] = false;
                    }
                }
                else {
                    notP += nums[i];
                }
            }

        }

        return abs(P - notP);
    }
};