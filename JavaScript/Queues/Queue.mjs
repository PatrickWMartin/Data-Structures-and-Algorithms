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
            this.length--;
            return this.values.remove();
        }
    }
    peek(){
        return this.values.head.data;
    }
    printList(){
        this.values.printList();
    }

}
