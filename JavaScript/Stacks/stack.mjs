import {LinkedList} from '../LinkedLists/linkedlist.mjs';


class Stack{
    constructor(){
       this.values = new LinkedList();
    }

    push(data){
        this.values.add(data);
    }

    pop(){
        return this.values.remove();
    }

    printStack(){
        this.values.printList();
    }
}

const stack = new Stack();
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
