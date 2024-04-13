# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution {
public:
    int subtractProductAndSum(int n) {

    int suma = 0;
int product = 1;
while (1 <= n){
suma += n% 10;
product *= n % 10;
n /= 10;
}

return product - suma;
}
};