package Java;

import java.util.Scanner;

public class DaysoBT {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        DaySo d = new DaySo(n);
        d.nhap(in);
        d.viet();
        System.out.println("max:" + d.max());
    }

    class DaySo {

        private double[] a;

        public DaySo(int n) {
            a = new double[n];
        }

        public void nhap(Scanner in) {
            for (int i = 0; i < a.length; i++) {
                a[i] = in.nextDouble();
            }
        }

        public void viet() {
            for (double x : a) {
                System.out.print(x + " ");
            }
            System.out.println();
        }

        public double max() {
            double m = a[0];
            for (int i = 1; i < a.length; i++) {
                if (a[i] > m) {
                    m = a[i];
                }
            }
            return m;
        }

    }
}
