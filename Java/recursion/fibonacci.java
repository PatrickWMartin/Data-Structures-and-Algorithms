class Fibonacci{
    public static int fibonacci(int n) {
        if (n <= 2){
            return 1;
        } else {
            return fibonacci(n-1) + fibonacci(n-2);
        }
    }
    public static void main(String []args) {
        int result = fibonacci(6);
        System.out.println(result); 
    }
}
