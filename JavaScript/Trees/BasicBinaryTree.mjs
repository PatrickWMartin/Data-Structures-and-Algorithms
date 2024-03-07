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
        const newNode = new BTNode(data);

        if (this.root === null){
            this.root = newNode;
            return;
        }

        const nodeQueue = new Queue();
        nodeQueue.enqueue(this.root);
        while (nodeQueue.length > 0) {
            let curr = nodeQueue.peek();

            if (curr.left === null){
                curr.left = newNode;
                return;
            }

            nodeQueue.enqueue(curr.left);

            if (curr.right === null){
                curr.right = newNode;
                return;
            }
            nodeQueue.enqueue(curr.right);
            nodeQueue.dequeue();
        }

    }

    //delete
    //in,pre,post traverse

}

const tree = new BasicBinaryTree();

tree.insert(1);
tree.insert(2);
tree.insert(3);
tree.insert(4);
tree.insert(5);
console.log(tree);
