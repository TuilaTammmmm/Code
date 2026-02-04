package Java;
import java.util.Scanner;

public class J01004 {

    public static Scanner sc = new Scanner(System.in);
    public static void SNT(int n){
        int count=0;
        for(int i=2;i*i<n;i++)
        {
            if(n%i==0)
            {
                count++;
            }
        }
        if(count>0)
        {
            System.out.println("NO");
        }
        else{
            System.out.println("YES");
        }
    }
    public static void main(String[] args) {
        int t = sc.nextInt();
        while (t-- > 0) {
            int n=sc.nextInt();
            SNT(n);
        }
    }
}