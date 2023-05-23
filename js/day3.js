// https://leetcode.com/problems/counter-ii/?utm_campaign=PostD3&utm_medium=Post&utm_source=Post&gio_link_id=xRxVYOXo

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

class Count{
    constructor(a){
        this.a= a;
        this.original = a;
    }

    increment(){

        return ++this.a;
    }

    decrement(){
        return --this.a;
    }

    reset(){
        this.a = this.original;
        return this.a;
    }
}

var createCounter = function(init) {
    return new Count(init);
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */