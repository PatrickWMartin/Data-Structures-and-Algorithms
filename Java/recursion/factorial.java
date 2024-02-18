class Factorial{
    public static int factorial(int num) {
        if (num == 1){
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }
    public static void main(String []args) {
        int result = factorial(5);
        System.out.println(result); 
    }
}
