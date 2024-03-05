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

const queue = new Queue();
console.log('New Queue');
queue.printList();
console.log('Add some values');
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(4);
queue.enqueue(5);
queue.printList();
console.log('remove some values');
queue.dequeue();
queue.dequeue();
queue.printList();
