class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}


class LinkedList{
    constructor(head = null){
        this.head = head;
    }
    
    /**
     * Add a new value to the front of the linked list
     * @param {any} data A value you want to add to the list 
     */
    add(data){
        const newNode = new Node(data); 
        newNode.next = this.head
        this.head = newNode;
    }

    /**
     * Remove the value from the front of the list
     */
    remove(){
        this.head = this.head.next;
    }

    /**
    * Print out what the current structure of the list looks like
    */
    printList(){
        let current = this.head;
        while (current !== null){
            process.stdout.write(`${current.data} -> `);
            current = current.next;
        }
        process.stdout.write('NULL\n');
    }

}


const list = new LinkedList();
list.add(1);
list.add(2);
list.add(3);
list.add(4);
list.add(5);
list.printList();
list.remove();
list.add(6);
list.printList();
