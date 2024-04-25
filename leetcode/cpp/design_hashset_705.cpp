
//https://leetcode.com/problems/design-hashset/description/


class MyHashSet {
private:
    int size = 1000;
    vector<vector<int>> bucket;
public:
    MyHashSet() {
        bucket.resize(size);
    }

    void add(int key){
        int position = key%size;
        if (contains(key)){
            return;
        }
        bucket[position].push_back(key);
    }

    void remove(int key) {
        int position = key%size;
        if (!contains(key)){
            return;
        }else{

            for(int i = 0; i < bucket[position].size(); i++){
                if (key == bucket[position][i]){
                    bucket[position][i] = -1; // faster since it just mark element as delete but it doesn't move it.
                    // bucket[position].erase(bucket[position].begin() + i); // recovers spaces
                }
            }
        }
    }
    bool contains(int key) {
        int position = key%size;
        for(int i = 0; i < bucket[position].size(); i++){
            if(find(bucket[position].begin(), bucket[position].end(), key) != bucket[position].end()) {
                return true;
            }
        }
        return false;
    };

};
/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */