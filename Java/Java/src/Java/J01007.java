package Java;



import java.util.Scanner;

public class J01007 {
    public static Scanner sc = new Scanner(System.in);

    public static boolean isFibonacci(long n) {
        if (n == 0 || n == 1) return true;
        long f1 = 0, f2 = 1;
        while (f2 < n) {
            long next = f1 + f2;
            f1 = f2;
            f2 = next;
        }
        return f2 == n;
    }

    public static void main(String[] args) {
        int t = sc.nextInt();
        while (t-- > 0) {
            long n = sc.nextLong();
            if (isFibonacci(n)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
