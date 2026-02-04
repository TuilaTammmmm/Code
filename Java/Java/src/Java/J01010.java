package Java;

import java.util.Scanner;

public class J01010 {

    public static Scanner sc = new Scanner(System.in);

    public static void ChiaDoi(int n) {
        int[] A = new int[20];
        int i=0;
        int dem=0;
        while (n > 0) {
            A[i]=n%10;
            n/=10;
            i++;
            dem++;
        }
        for(int j=dem;j=0;j++)
        {
            if(A[j]>0)
            {
                for(int k=dem;k=0;k++)
                {
                    System.out.print(A[k]);
                }
            }
        }
    }

    public static void main(String[] args) {
        int t = sc.nextInt();
        int i = 1;
        while (t-- > 0) {
            int n = sc.nextInt();
            ChiaDoi(n);
        }
    }
}
