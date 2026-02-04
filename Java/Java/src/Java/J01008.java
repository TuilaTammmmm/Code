package Java;

import java.util.Scanner;

public class J01008 {

    public static Scanner sc = new Scanner(System.in);

    public static void PT(int n) {
        for (int j = 2; j <= n; j++) {
            int dem = 0;
            while (n % j == 0) {
                dem++;
                n /= j;
            }
            if (dem > 0) {
                System.out.print(j + "(" + dem + ")");
                System.out.print(" ");
            }
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        int t = sc.nextInt();
        int i = 1;
        while (t-- > 0) {
            int n = sc.nextInt();
            System.out.print("Test " + i + ": ");
            PT(n);
            i++;
        }
    }
}
