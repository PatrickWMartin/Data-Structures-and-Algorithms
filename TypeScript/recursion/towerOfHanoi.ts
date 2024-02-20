function towerOfHanoi(n: number, source: string, helper: string, destination: string): void{
    if (n === 0){
        return;
    }
    towerOfHanoi(n-1, source, destination, helper);
    console.log(`Disk ${n} from rod ${source} to rod ${destination}`);
    towerOfHanoi(n-1, helper, source, destination);
}

towerOfHanoi(3, 'A', 'B', 'C');
