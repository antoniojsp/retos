function foo(n){

    if (n <= 0){
        return;
    };
    console.log("hola:" + n);
    foo(n-1);
    foo(n-1);
    foo(n-1);

};

foo(3);
console.log("ya")