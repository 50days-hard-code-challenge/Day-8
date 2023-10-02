class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
          vector<int>dup(n);
            for(int i=0;i<n;i++){
                dup[(i+k)%n]=nums[i];
            }
        nums=dup;
    }
};
