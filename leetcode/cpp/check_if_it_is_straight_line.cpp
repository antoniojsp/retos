

//https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x1 = coordinates[0][0];
        int y1 = coordinates[0][1];
        int x2 = coordinates[1][0];
        int y2 = coordinates[1][1];

        double slope;
        if (x1 == x2){
            slope = numeric_limits<double>::infinity();
        }else{
            slope = (y1-y2)/(double)(x1-x2);
        }
        cout << "first " << slope<<endl;
        int i = 1;

        while (i < coordinates.size()-1){

            int x1 = coordinates[i][0];
            int y1 = coordinates[i][1];
            int x2 = coordinates[i+1][0];
            int y2 = coordinates[i+1][1];
            double curr_slope;
            i++;
            if(x1 == x2){
                curr_slope = numeric_limits<double>::infinity();
            }else{
                curr_slope = (y1-y2)/(double)(x1-x2);
            }
            cout << curr_slope <<endl;
            if(slope != curr_slope){
                return false;
            }

        }

        return true;
    }
};