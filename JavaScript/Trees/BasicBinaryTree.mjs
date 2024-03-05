import {Queue} from '../Queues/Queue.mjs';

class BTNode{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BasicBinaryTree{
    constructor(){
        this.root = null;
    }

    insert(data){
        const newNode = BTNode(data);

        if (this.root === null){
            this.root = newNode;
            return;
        }

        const nodeQueue = Queue();
        nodeQueue.enqueue(this.root);
        

    }


    //insert
    //delete
    //in,pre,post traverse

}
