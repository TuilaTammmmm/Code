package Java;

import java.util.Scanner;

public class J01001 {
    public static Scanner sc = new Scanner(System.in);
    public static void HCN(int a,int b){
        int CV=2*(a+b);
        int DT=a*b;
        System.out.print(CV +" "+DT);
    }
    public static void main(String[] args) {
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a<=0 || b<=0){
            System.out.print("0");
            }
        else{
            HCN(a,b);
            }
        sc.close();
    }
}
