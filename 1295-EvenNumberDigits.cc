// Problem #1295. Find Numbers with Even Number of Digits

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (vector<int>::iterator it = nums.begin() ; it != nums.end(); ++it) {
            if (isEven(*it)) {
                count++;
            }
        }
        return count;
    }
    
    bool isEven(int &num) {
        if (num/10 == 0) {
            return false;
        }
        int count = 1;
        int numCopy = num;
        while (numCopy/10 != 0) {
            count++;
            numCopy = (numCopy/10);
        }
        return (count % 2 == 0) ? true : false;
    }
};
