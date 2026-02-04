package Java;

import java.util.Scanner;

public class MaTran1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        MaTran m = new MaTran(n);
        m.input(in);

        MaTran b = m.chuyenvi();
        b.output();
    }
}

class MaTran {
    private int[][] a;

    public MaTran(int n) {
        a = new int[n][n];
    }

    public MaTran(int[][] a) {
        this.a = a;
    }

    public void input(Scanner in) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                a[i][j] = in.nextInt();
            }
        }
    }

    public void output() {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }

    public MaTran tong(int[][] b) {
        int[][] t = new int[a.length][a.length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                t[i][j] = a[i][j] + b[i][j];
            }
        }
        return new MaTran(t);
    }

    public MaTran tich(int[][] b) {
        int[][] t = new int[a.length][a.length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                for (int k = 0; k < a.length; k++) {
                    t[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return new MaTran(t);
    }

    public MaTran chuyenvi() {
        int t[][] = new int[a.length][a.length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                t[j][i] = a[i][j];
            }
        }
        return new MaTran(t);
    }
    public int[] tongHang() {
        int t[] = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                t[i]+=a[i][j];
            }
        }
        return t;
    }
}
