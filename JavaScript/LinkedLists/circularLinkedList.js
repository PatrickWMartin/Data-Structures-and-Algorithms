class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class CircularLinkedList{
    constructor(){
        this.head = null;
        //I like using a tail pointer with circular linked list because it 
        //allows us to do inserts in O(1) time. Without the tail pointer we would need
        //to loop to the end of the list to get a reference to last pointer and change the next pointer.
        this.tail = null;
        this.length = 0;
    }

    add(data){
        const newNode = new Node(data);
        
        if (this.head === null){ 
            this.head = newNode;
            this.tail = newNode;
        } else{
            newNode.next = this.head;
            this.head = newNode;
        }
        this.tail.next = this.head;
        this.length++;
    }

    remove(){
        this.tail.next = this.head.next;
        this.head = this.head.next;
        this.length--;
    }

    printList(){
        let current = this.head;
        let i = 0;
        while (i < this.length){
            process.stdout.write(`${current.data} -> `);
            current = current.next;
            i++;
        }
        process.stdout.write('NULL\n');
    }


}

const list = new CircularLinkedList();
console.log('New Linked List');
list.printList();
console.log('Add some values');
list.add(1);
list.add(2);
list.add(4);
list.add(5);
list.printList();
console.log('remove some values');
list.remove();
list.remove();
list.remove();
list.printList();
