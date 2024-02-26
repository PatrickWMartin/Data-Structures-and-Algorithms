class ListStack{
    constructor(){
        this.values = []; 
    }

    push(data){
        this.values.push(data);
    }

    pop(){
        return this.values.pop()
    }

    printStack(){
        console.log(this.values);
    }

}

const stack = new ListStack();
stack.pop();
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
stack.printStack();
stack.pop();
stack.pop();
stack.printStack();
let x = stack.pop();
console.log(x);
stack.printStack();
