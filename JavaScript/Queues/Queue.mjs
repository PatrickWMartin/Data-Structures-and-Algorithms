import {LinkedListTail} from '../LinkedLists/LinkedListTail.mjs';

export class Queue{
    constructor(){
        this.values = new LinkedListTail();
        this.length = 0;
    }

    enqueue(data){
        this.values.add(data);
        this.length++;
    }
    dequeue(){
        if (this.length > 0){
            this.values.remove();
            this.length--;
        }
    }
    peek(){
        return this.values.tail.data;
    }
    printList(){
        this.values.printList();
    }

}
