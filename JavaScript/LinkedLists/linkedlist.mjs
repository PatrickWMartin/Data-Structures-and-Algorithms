class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}


export class LinkedList{
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
               
        // if somehting wants to be added to index 0 just call add
        // or the list is empty
        if (index === 0 || this.head === null){
            this.add(data);
            return;
        }

        let current = this.head;
        let i = 0;

        while(current !== null){
            if(i === index-1){
                newNode.next = current.next;
                current.next = newNode;
                break; 
            }
            current = current.next;
            i++;
        }
    }
   
    /**
     * Remove a value from any position in the list
     * @param {number} index The index to insert the value at 
     */

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
