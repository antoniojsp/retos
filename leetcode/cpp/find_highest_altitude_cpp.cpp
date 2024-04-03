#include <numeric>

class Solution {
public:
    int largestAltitude(vector<int>& gain) {

        int current_altitude = 0;
        int max_altitude = current_altitude;
        for(auto i = 0; i < gain.size(); i++){
            current_altitude += gain[i];
            max_altitude = max(max_altitude, current_altitude);
        }

        return max_altitude;
    }
};