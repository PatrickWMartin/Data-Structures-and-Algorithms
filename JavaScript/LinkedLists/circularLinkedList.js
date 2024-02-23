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
        const newNode = newNode(data);
        
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



}
