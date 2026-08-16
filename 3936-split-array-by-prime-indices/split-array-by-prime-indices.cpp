#include <cstdlib>
using namespace std;

class Solution {
public:
    long long splitArray(vector<int>& nums) {
        long long sum = 0, n = nums.size();
        vector<bool> primes(n, true);

        primes[0] = false;
        if (1 < n) {
            primes[1] = false;       
        }
        
        for(int i = 2; i * i < n; i += 1) {
            if(not primes[i]) continue;
            for(int j = i * i; j < n; j += i) {
                primes[j] = false;
            }
        }

        for(int i = 0; i < nums.size(); i++) {
            if (primes[i]) {
                sum += nums[i];
            }
            else {
                sum -= nums[i];
            }

        }

        return abs(sum);
    }
};