import java.util.Scanner;
//Without using recursion
// class Fib{
//     public static void main(String args [] ){
//         int n1 = 0;
//         int n2 = 1;
//         int n3;
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter the number of terms: ");
//         int count = sc.nextInt();
//         System.out.println(n1+" "+n2);
//         for(int i=2;i<=count;i++){
//             n3 = n1 + n2;
//             System.out.println(n3);
//             n1 = n2;
//             n2 = n3;
//         }
//         sc.close();
//     }
// }

//Using recursion
class Fib{
    static int n1=0,n2=1,n3=0;
    public void printFib(int count){
        if(count>0){
            n3 = n1 + n2;
            System.out.println(""+n3);
            n1=n2;
            n2=n3;
            printFib(count-1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of terms: ");
        int count = sc.nextInt();
        System.out.println(n1);
        System.out.println(n2);
        Fib f = new Fib();
        f.printFib(count-2);
        sc.close();
    }
}
