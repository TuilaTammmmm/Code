package Java;

import java.util.Scanner;

public class J01006 {
    public  static Scanner sc=new Scanner(System.in);
    public static long A[]= new long[100];
    public static void Fibonacci() {
        A[1]=A[2]=1;
        for(int i=3;i<=92;i++)
            A[i]=A[i-1]+A[i-2];
    }

    public static void main(String[] args) {
        Fibonacci();
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            System.out.println(A[n]);
        }
        sc.close();
    }
}
