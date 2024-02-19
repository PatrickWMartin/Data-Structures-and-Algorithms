package main
import "fmt"

func towerOfHanoi(n int, source string, helper string, destination string)  {
    if n == 0{
        return
    } 
    towerOfHanoi(n-1, source, destination, helper)
    fmt.Printf("Disk %d from rod %s to rod %s\n", n, source, destination)
    towerOfHanoi(n-1, helper, source, destination)
}
func main() {
   towerOfHanoi(3, "A","B","C") 
}
