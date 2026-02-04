package Java;

import java.io.*;
import java.util.*;

public class DonHang {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());
        List<CTDonHang> a = new ArrayList<>();
        List<Hang> b;
        for (int i = 0; i < n; i++) {
            String hoten = in.nextLine();
            String sdt = in.nextLine();
            String ngaymua = in.nextLine();
            int m = Integer.parseInt(in.nextLine());
            b = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                String tenhang = in.nextLine();
                int sl = Integer.parseInt(in.nextLine());
                double gia = Double.parseDouble(in.nextLine());
                b.add(new Hang(tenhang, sl, gia));
            }
            a.add(new CTDonHang(hoten, sdt, ngaymua, b));
        }
        int c = 0;
        String ma = in.nextLine();
        for (CTDonHang i : a) {
            if (i.getMa().equalsIgnoreCase(ma)) {
                System.out.println(i);
                String ten = in.nextLine();
                i.setHoten(ten);
                String mamoi = "";
                String[] s = ten.trim().toUpperCase().split("\\s+");
                for (String k : s) {
                    mamoi += k.charAt(0);
                }
                int vt = 0;
                for (int j = 0; j < ma.length(); j++) {
                    if (Character.isDigit(ma.charAt(j))) {
                        vt = j;
                        break;
                    }
                }
                mamoi += ma.substring(vt);
                i.setMa(mamoi);
                c++;
                System.out.println(i);
                break;
            }
        }
        if (c == 0) {
            System.out.println("khong co don hang");
        }
    }
}

class Hang {

    private String ma, ten;
    private int soluong;
    private double gia;
    private static int sma = 1;

    public Hang() {
    }

    public Hang(String ten, int soluong, double gia) {
        this.ma = "MH" + String.format("%03d", sma++);
        this.ten = ten;
        this.soluong = soluong;
        this.gia = gia;
    }

    public double gettien() {
        return soluong * gia;
    }
}

class CTDonHang {

    private String ma, hoten, sdt, ngaymua;
    private List<Hang> dsHang;
    private double tongtien;
    private static int sma = 1;

    public CTDonHang() {
    }

    public String getMa() {
        return ma;
    }

    public void setMa(String ma) {
        this.ma = ma;
    }

    public void setHoten(String hoten) {
        this.hoten = hoten;
    }

    public CTDonHang(String hoten, String sdt, String ngaymua, List<Hang> dsHang) {
        this.hoten = hoten;
        this.ma = taoMa(hoten);
        this.sdt = sdt;
        this.ngaymua = ngaymua;
        this.dsHang = dsHang;
        this.tongtien = getTongTien(dsHang);
    }

    private String taoMa(String hoten) {
        String[] s = hoten.trim().toUpperCase().split("\\s+");
        String st = "";
        for (String i : s) {
            st += i.charAt(0);
        }
        st += String.format("%03d", sma++);
        return st;
    }

    private double getTongTien(List<Hang> a) {
        double tong = 0;
        for (Hang hang : a) {
            tong += hang.gettien();
        }
        return tong;
    }

    @Override
    public String toString() {
        return ma + " " + hoten + " " + ngaymua + " " + Math.round(tongtien);
    }
}
