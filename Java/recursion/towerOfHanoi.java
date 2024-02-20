class TowerOfHanoi {
    public static void towerOfHanoi(int n, String source, String helper, String destination) {
        if (n == 0){
            return;
        }
        towerOfHanoi(n-1, source, destination, helper);
        System.out.format("Disk %d from rod %s to rod %s\n", n, source, destination);
        towerOfHanoi(n-1, helper, source, destination);
    }
    public static void main(String []args) {
        towerOfHanoi(3,"A","B","C"); 
    }
}
