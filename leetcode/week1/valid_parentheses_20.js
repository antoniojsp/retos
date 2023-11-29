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
        return this.arr.length == 0;
    }

    print(){
        console.log(this.arr)
    }
};


function isValid(s){
    store = new Stack()
    var map = {"[":"]", "{":"}", "(":")"}
    for (i of s){
        // console.log(store.print())
        if (i in map){
            store.push(i)
        }else{
            var last = store.pop()
            if(map[last] != i){
                return false
            }
        }
    };
    return store.isEmpty()

};
// {[{}]}
//{[](){()}}
console.log(isValid("{[{}}]}"))