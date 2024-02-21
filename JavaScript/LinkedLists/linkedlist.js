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
        // This may look weird and too simple to get rid of the front of the list but this is really all we have to do.
        // In javascript the garabage collector will come by and get rid of an object when it is no longer accessible or 
        // usable somehow aka it is no longer reachable. So once we change the head of the list to the next node in the list
        // The previous head is no longer reachable and will be dealt with in garbage collection. 
        this.head = this.head.next;
    }
    
    /**
     * Add a new value at any position in the list
     * @param {number} index The index to insert the value at 
     * @param {any} data The data to be added
     */
    insertAt(data, index){
        const newNode = new Node(data); 

        if (this.head == null)
            return;
       
        //if somehting wants to be added to index 0 just call add
        if (index == 0){
            this.add(data);
            return;
        }

        let current = this.head;
        let i = 0;

        while(current != null){
            if(i == index-1){
                newNode.next = current.next;
                current.next = newNode;
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
            process.stdout.write(`${current.data} -> `);
            current = current.next;
        }
        process.stdout.write('NULL\n');
    }

}


const list = new LinkedList();
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
