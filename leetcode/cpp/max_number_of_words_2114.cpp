
//https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {

        int result = 0;

        for(int i = 0; i<sentences.size(); i++){
            string current = sentences[i];
            int count = 0;
            for(int j = 0; j<current.size(); j++){
                if(current[j] == ' '){
                    count++;
                }
            }
            result = count > result? count: result;

        }


        return result + 1;

    }
};

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {

        int result = 0;

        for(int i = 0; i<sentences.size(); i++){
            string current = sentences[i];
            int num = count(current.begin(),current.end(),' ');
            result = num > result? num: result;

        }
        return result + 1;

    }
};