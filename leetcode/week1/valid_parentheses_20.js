class Stack{

    constructor(){
        this.arr = [];
    };

    push(value){
        this.arr.push(value);
    }
    peek(){
        return this.arr[this.arr.length-1];
    }
    pop(){
        return this.arr.pop();
    }

    isEmpty(){
        return this.arr.length > 0;
    }

    print(){
        console.log(this.arr)
    }
};


function isValid(s){
    store = new Stack()
    for (i of s){

    };

};
// {[{}]}
isValid("antonio")