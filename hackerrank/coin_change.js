var change = function(amount, coins) {
    function helper(a, c, memo = {}){
        if (a == 0){
            return 1
        };
        if(a < 0){
            return 0
        };
        var name = a + "#" +c.length;
        if (name in memo){

            return memo[name]
        };

        var total = 0;
        for(var i = 0; i < c.length; i++){

            var coin = c[i];
            if (coin > a){
                continue;
            };
             total += helper(a - coin, c.slice(i), memo);
        };
        memo[name] = total
        return memo[name]
    };
    return helper(amount, coins);
};