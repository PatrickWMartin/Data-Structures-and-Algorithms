import {LinkedListTail} from '../LinkedLists/LinkedListTail.mjs';

export class Queue{
    constructor(){
        this.values = new LinkedListTail();
    }

    enqueue(data){
        this.values.add(data);
    }
    dequeue(){
        this.values.remove();
    }
    printList(){
        this.values.printList();
    }

}
