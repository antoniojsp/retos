class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {

        double first_slope;

        int i = 0;
        while (i < coordinates.size()-1){
            int x1 = coordinates[i][0];
            int y1 = coordinates[i][1];
            int x2 = coordinates[i+1][0];
            int y2 = coordinates[i+1][1];

            if(i == 0){
                if(x1 == x2){
                    first_slope = numeric_limits<double>::infinity();
                }else{
                    first_slope = (y1-y2)/(double)(x1-x2);
                }
            }else{
                double curr_slope = (x1 == x2)?numeric_limits<double>::infinity():(y1-y2)/(double)(x1-x2);
                if(first_slope != curr_slope){
                    return false;
                }
            }
            i++;
        }

        return true;
    }
};