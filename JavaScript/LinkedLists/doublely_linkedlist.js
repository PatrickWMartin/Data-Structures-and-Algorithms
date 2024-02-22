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

    remove(){
        this.head = this.head.next;
        this.head.prev = null;
    }

    insertAt(data, index){
        const newNode = new Node(data); 
               
        if (index === 0 || this.head === null){
            this.add(data);
            return;
        }

        let current = this.head;
        let i = 0;

        while(current !== null){
            if(i === index-1){
                newNode.next = current.next;
                current.next.prev = newNode;
                
                newNode.prev = current
                current.next = newNode;
                break; 
            }
            current = current.next;
            i++;
        }
    }
    
    removeAt(index){
        if(this.head === null)
            return;

        if (index === 0){
            this.remove();
            return;
        }
        
        let current = this.head;
        let i = 0;
        while(current !== null){
            if(i === index-1){
                current.next = current.next.next;
                if (current.next)
                    current.next.prev = current;
                break; 
            }
            current = current.next;
            i++;
        }

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
list.add(4);
list.add(5);
list.printList();
console.log('Insert 3 at index 2');
list.insertAt(3,2);
list.printList();
console.log('remove some values');
list.remove();
list.remove();
list.remove();
list.printList();
console.log('Add some more values');
list.add(6);
list.add(7);
list.add(8);
list.printList();
console.log('remove last element');
list.removeAt(4);
list.printList();
