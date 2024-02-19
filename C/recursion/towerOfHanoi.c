#include <stdio.h>

void towerOfHanoi(int n, char source, char helper, char destination){
    if (n == 0){
        return;
    }
    towerOfHanoi(n-1, source, destination, helper);
    printf("Disk %d from rod %c to rod %c\n", n, source, destination);
    towerOfHanoi(n-1, helper, source, destination);
}

int main(){
    towerOfHanoi(3, 'A', 'B', 'C');
    return 0;
}
