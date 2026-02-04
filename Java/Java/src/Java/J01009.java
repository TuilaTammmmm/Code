package Java;

import java.util.Scanner;

public class J01009 {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt();
        long fac = 1;
        long sum = 0;

        for (int i = 1; i <= n; i++) {
            fac *= i;
            sum += fac;
        }

        System.out.print(sum);
    }
}
