class Node{
    constructor(data){
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoubleyLinkedList{
    constructor(head = null){
        this.head = head;
    }

    add(data){
        const newNode = new Node(data);
        newNode.next = this.head;

        if(this.head !== null)
            this.head.prev = newNode
        
        this.head = newNode;
    }

    remove(data){
        this.head = this.head.next;
        this.head.prev = null;
    }

    /**
    * Print out what the current structure of the list looks like
    */
    printList(){
        let current = this.head;
        while (current !== null){
            process.stdout.write(`${current.data} <-> `);
            current = current.next;
        }
        process.stdout.write('NULL\n');
    }
}

const list = new DoubleyLinkedList();
console.log('New Linked List');
list.printList();
console.log('Add some values');
list.add(1);
list.add(2);
list.add(3);
list.add(4);
list.printList();
