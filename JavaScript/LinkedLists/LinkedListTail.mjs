class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

export class LinkedListTail{
    constructor(){
        this.head = null;
        this.tail = null;
    }

    add(data){
        const newNode = new Node(data);
        if (this.tail === null){
            this.head = newNode;
        } else{
            this.tail.next = newNode;
        }
        this.tail = newNode
    }

    remove(){
        this.head = this.head.next;
    } 

     printList(){
        let current = this.head;
        while (current !== null){
            process.stdout.write(`${current.data} -> `);
            current = current.next;
        }
        process.stdout.write('NULL\n');
    }
}
