
import java.util.Random;
import java.util.Scanner;

public class sinhvien {
    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);
        dayso d = new dayso(ip.nextInt());
        d.input(ip);
        d.out();
        System.out.println("-----------");
        System.out.println("max:"+d.max());
        System.out.println("min:"+d.min());
        System.out.println("sum:"+d.sum());
        System.out.println("chia het cho 7:"+d.chiahetcho7());
    }
}

class dayso {

    private final int[] a;

    public dayso(int n) {
        a = new int[n];
    }

    public int[] getA() {
        return a;
    }

    public void input(Scanner in) {
        for (int i = 0; i < a.length; i++) {
            a[i] = in.nextInt();
        }
    }

    public void out() {
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i] + " ");
        }
    }

    public int max() {
        int t = a[0];
        for (int i = 1; i < a.length; i++) {
            if (a[i] > t) {
                t = a[i];
            }
        }
        return t;
    }
    public int min() {
        int t = a[0];
        for (int i = 1; i < a.length; i++) {
            if (a[i] < t) {
                t = a[i];
            }
        }
        return t;
    }
    public int sum() {
        int t = a[0];
        for (int i = 0; i < a.length; i++) {
            if (a[i] > t) {
                t += a[i];
            }
        }
        return t;
    }
    public int chiahetcho7(){
        int t = a[0];
        for (int i = 0; i < a.length; i++) {
            if (a[i] > t) {
                t += a[i];
            }
        }
        return t;
    }
    private boolean isNT(int n) {
        if (n <= 1) {
            return false;
        } else {
            for (int i = 0; i <= Math.sqrt(n); i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
    }
    
    public int[] dayNT() {
        int c = 0;
        for (int i = 0; i < a.length; i++) {
            if (isNT(a[i])) {
                c++;
            }
        }
        int[] t = new int[c];
        int k = 0;
        for (int i = 0; i < a.length; i++) {
            if (isNT(a[i])) {
                nt[k++] = a[i];
            }
        }
    }
}
